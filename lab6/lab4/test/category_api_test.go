package test

import (
	"bytes"
	"encoding/json"
	"github.com/labstack/echo/v4"
	"github.com/stretchr/testify/assert"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"lab4/controllers"
	"lab4/models"
	"lab4/routes"
	"lab4/service"
	"net/http"
	"net/http/httptest"
	"testing"
)

func setupCategoryTestServer() (*echo.Echo, *service.CategoryService) {
	db, _ := gorm.Open(sqlite.Open(":memory:"), &gorm.Config{})
	db.AutoMigrate(&models.Category{}, &models.Product{})
	
	categoryService := &service.CategoryService{DB: db}
	categoryController := &controllers.CategoryController{CategoryService: categoryService}

	e := echo.New()
	routes.CategoryRouter(categoryController, e)

	return e, categoryService
}

func TestCreateCategory(t *testing.T) {
	e, _ := setupCategoryTestServer()

	t.Run("Success", func(t *testing.T) {
		body := map[string]string{
			"name": "Test Category",
		}
		jsonBody, _ := json.Marshal(body)

		req := httptest.NewRequest(http.MethodPost, "/category", bytes.NewBuffer(jsonBody))
		req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)

		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusCreated, rec.Code)
	})

	t.Run("Invalid JSON", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodPost, "/category", bytes.NewBufferString("{invalid json}"))
		req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)

		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}

func TestGetAllCategories(t *testing.T) {
	e, categoryService := setupCategoryTestServer()

	categoryService.CreateCategory(models.Category{Name: "Sample Category"})

	req := httptest.NewRequest(http.MethodGet, "/category", nil)
	rec := httptest.NewRecorder()
	e.ServeHTTP(rec, req)

	assert.Equal(t, http.StatusOK, rec.Code)
}

func TestGetCategoryByID(t *testing.T) {
	e, categoryService := setupCategoryTestServer()

	category := models.Category{Name: "Test Category"}
	categoryService.CreateCategory(category)

	t.Run("Success", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodGet, "/category/1", nil)
		rec := httptest.NewRecorder()

		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusOK, rec.Code)
	})

	t.Run("Invalid ID format", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodGet, "/category/abc", nil)
		rec := httptest.NewRecorder()

		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}

func TestUpdateCategory(t *testing.T) {
	e, categoryService := setupCategoryTestServer()

	category := models.Category{Name: "Old Name"}
	categoryService.CreateCategory(category)

	t.Run("Success", func(t *testing.T) {
		updatedCategory := models.Category{Name: "Updated Name"}
		jsonBody, _ := json.Marshal(updatedCategory)

		req := httptest.NewRequest(http.MethodPut, "/category", bytes.NewBuffer(jsonBody))
		req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)

		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusOK, rec.Code)
	})

	t.Run("Invalid JSON", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodPut, "/category", bytes.NewBufferString("{invalid json}"))
		req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)

		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}

func TestDeleteCategory(t *testing.T) {
	e, categoryService := setupCategoryTestServer()

	category := models.Category{Name: "ToDelete"}
	categoryService.CreateCategory(category)

	t.Run("Success", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodDelete, "/category/1", nil)
		rec := httptest.NewRecorder()

		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusOK, rec.Code)
	})

	t.Run("Invalid ID format", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodDelete, "/category/abc", nil)
		rec := httptest.NewRecorder()

		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}
