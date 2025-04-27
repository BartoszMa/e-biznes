package test

import (
	"lab4/models"
	"lab4/service"
	"testing"

	"github.com/stretchr/testify/assert"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func SetupCategoryTestDB() *gorm.DB {
	db, err := gorm.Open(sqlite.Open(":memory:"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}
	db.AutoMigrate(&models.Category{}, &models.Product{})
	return db
}

func TestCategoryService_CreateCategory(t *testing.T) {
	db := SetupCategoryTestDB()
	svc := service.CategoryService{DB: db}

	category := models.Category{Name: "Electronics"}

	err := svc.CreateCategory(category)
	assert.NoError(t, err)

	var check models.Category
	err = db.First(&check, "name = ?", "Electronics").Error
	assert.NoError(t, err)
	assert.Equal(t, "Electronics", check.Name)
}

func TestCategoryService_GetAllCategories(t *testing.T) {
	db := SetupCategoryTestDB()
	svc := service.CategoryService{DB: db}

	db.Create(&models.Category{Name: "Books"})
	db.Create(&models.Category{Name: "Clothes"})

	categories, err := svc.GetAllCategories()

	assert.NoError(t, err)
	assert.Len(t, categories, 2)
	assert.Equal(t, "Books", categories[0].Name)
	assert.Equal(t, "Clothes", categories[1].Name)
}

func TestCategoryService_GetCategoryByID(t *testing.T) {
	db := SetupCategoryTestDB()
	svc := service.CategoryService{DB: db}

	newCategory := models.Category{Name: "Games"}
	db.Create(&newCategory)

	fetched, err := svc.GetCategoryByID(newCategory.ID)

	assert.NoError(t, err)
	assert.Equal(t, newCategory.ID, fetched.ID)
	assert.Equal(t, "Games", fetched.Name)
}

func TestCategoryService_UpdateCategory(t *testing.T) {
	db := SetupCategoryTestDB()
	svc := service.CategoryService{DB: db}

	category := models.Category{Name: "Food"}
	db.Create(&category)

	category.Name = "Groceries"
	err := svc.UpdateCategory(category)

	assert.NoError(t, err)

	var updated models.Category
	db.First(&updated, category.ID)
	assert.Equal(t, "Groceries", updated.Name)
}

func TestCategoryService_DeleteCategory(t *testing.T) {
	db := SetupCategoryTestDB()
	svc := service.CategoryService{DB: db}

	category := models.Category{Name: "Furniture"}
	db.Create(&category)

	err := svc.DeleteCategory(category.ID)
	assert.NoError(t, err)

	var deleted models.Category
	result := db.First(&deleted, category.ID)
	assert.Error(t, result.Error)
	assert.Equal(t, int64(0), result.RowsAffected)
}

func TestCategoryService_DeleteCategory_NotFound(t *testing.T) {
	db := SetupCategoryTestDB()
	svc := service.CategoryService{DB: db}

	err := svc.DeleteCategory(999)
	assert.Error(t, err)
	assert.Equal(t, "category not found", err.Error())
}
