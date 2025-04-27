package test

import (
	"lab4/models"
	"lab4/service"
	"testing"

	"github.com/stretchr/testify/assert"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func SetupProductTestDB() *gorm.DB {
	db, err := gorm.Open(sqlite.Open(":memory:"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}
	db.AutoMigrate(&models.Category{}, &models.Product{})
	return db
}

func TestProductService_AddProduct(t *testing.T) {
	db := SetupProductTestDB()
	svc := service.Service{DB: db}

	product := models.Product{Name: "Laptop", Price: 1200}

	err := svc.AddProduct(product)
	assert.NoError(t, err)

	var check models.Product
	err = db.First(&check, "name = ?", "Laptop").Error
	assert.NotZero(t, check.Price)
	assert.NotZero(t, check.ID)
	assert.Zero(t, check.CategoryID)
	assert.NoError(t, err)
	assert.Equal(t, "Laptop", check.Name)
	assert.Equal(t, float32(1200), check.Price)
}

func TestProductService_GetAllProducts(t *testing.T) {
	db := SetupProductTestDB()
	svc := service.Service{DB: db}

	db.Create(&models.Product{Name: "Book", Price: 20})
	db.Create(&models.Product{Name: "Shirt", Price: 50})

	products, err := svc.GetAllProducts()
	assert.NoError(t, err)
	assert.Len(t, products, 2)
	assert.Equal(t, "Book", products[0].Name)
	assert.Equal(t, "Shirt", products[1].Name)
}

func TestProductService_GetOneProduct_NotFound(t *testing.T) {
	db := SetupProductTestDB()
	svc := service.Service{DB: db}

	_, err := svc.GetOneProduct(999)
	assert.Error(t, err)
}

func TestProductService_GetOneProduct(t *testing.T) {
	db := SetupProductTestDB()
	svc := service.Service{DB: db}

	newProduct := models.Product{Name: "Keyboard", Price: 100}
	db.Create(&newProduct)

	fetched, err := svc.GetOneProduct(newProduct.ID)

	assert.NoError(t, err)
	assert.Equal(t, newProduct.ID, fetched.ID)
	assert.Equal(t, "Keyboard", fetched.Name)
	assert.Equal(t, float32(100), fetched.Price)
}

func TestProductService_EditProduct(t *testing.T) {
	db := SetupProductTestDB()
	svc := service.Service{DB: db}

	product := models.Product{Name: "Table", Price: 200}
	db.Create(&product)

	product.Price = 250
	err := svc.EditProduct(product)
	assert.NoError(t, err)

	var updated models.Product
	db.First(&updated, product.ID)
	assert.Equal(t, float32(250), updated.Price)
}

func TestProductService_RemoveProduct(t *testing.T) {
	db := SetupProductTestDB()
	svc := service.Service{DB: db}

	product := models.Product{Name: "Chair", Price: 80}
	db.Create(&product)

	err := svc.RemoveProduct(product.ID)
	assert.NoError(t, err)

	var deleted models.Product
	result := db.First(&deleted, product.ID)
	assert.Error(t, result.Error)
	assert.Equal(t, int64(0), result.RowsAffected)
}

func TestProductService_RemoveProduct_NotFound(t *testing.T) {
	db := SetupProductTestDB()
	svc := service.Service{DB: db}

	err := svc.RemoveProduct(999)
	assert.Error(t, err)
	assert.Equal(t, "product not found", err.Error())
}
