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

func setupProductTestServer() (*echo.Echo, *service.Service) {
	db, _ := gorm.Open(sqlite.Open(":memory:"), &gorm.Config{})
	db.AutoMigrate(&models.Category{}, &models.Product{})

	dbService := &service.Service{DB: db}
	productController := &controllers.ProductController{DbService: dbService}

	e := echo.New()
	routes.ProductRouter(productController, e)

	return e, dbService
}

func TestCreateProduct(t *testing.T) {
	e, dbService := setupProductTestServer()

	dbService.DB.Create(&models.Category{Name: "Test Category"})

	t.Run("Success", func(t *testing.T) {
		body := map[string]interface{}{
			"name":        "Test Product",
			"price":       10.5,
			"category_id": 1,
		}
		jsonBody, _ := json.Marshal(body)

		req := httptest.NewRequest(http.MethodPost, "/product", bytes.NewBuffer(jsonBody))
		req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)

		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusCreated, rec.Code)
	})

	t.Run("Invalid JSON", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodPost, "/product", bytes.NewBufferString("{invalid json}"))
		req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)

		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}

func TestGetAllProducts(t *testing.T) {
	e, dbService := setupProductTestServer()
	
	category := models.Category{Name: "Sample Category"}
	dbService.DB.Create(&category)
	dbService.DB.Create(&models.Product{Name: "Sample Product", Price: 20.0, CategoryID: category.ID})

	req := httptest.NewRequest(http.MethodGet, "/product", nil)
	rec := httptest.NewRecorder()
	e.ServeHTTP(rec, req)

	assert.Equal(t, http.StatusOK, rec.Code)
}

func TestGetProductByID(t *testing.T) {
	e, dbService := setupProductTestServer()

	category := models.Category{Name: "Test Category"}
	dbService.DB.Create(&category)
	product := models.Product{Name: "Test Product", Price: 15.0, CategoryID: category.ID}
	dbService.DB.Create(&product)

	t.Run("Success", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodGet, "/product/1", nil)
		rec := httptest.NewRecorder()

		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusOK, rec.Code)
	})

	t.Run("Invalid ID format", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodGet, "/product/abc", nil)
		rec := httptest.NewRecorder()

		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}

func TestUpdateProduct(t *testing.T) {
	e, dbService := setupProductTestServer()

	category := models.Category{Name: "Test Category"}
	dbService.DB.Create(&category)
	product := models.Product{Name: "Old Product", Price: 5.0, CategoryID: category.ID}
	dbService.DB.Create(&product)

	t.Run("Success", func(t *testing.T) {
		updatedProduct := map[string]interface{}{
			"ID":          1,
			"name":        "Updated Product",
			"price":       25.0,
			"category_id": category.ID,
		}
		jsonBody, _ := json.Marshal(updatedProduct)

		req := httptest.NewRequest(http.MethodPut, "/product", bytes.NewBuffer(jsonBody))
		req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)

		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusOK, rec.Code)
	})

	t.Run("Invalid JSON", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodPut, "/product", bytes.NewBufferString("{invalid json}"))
		req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)

		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}

func TestDeleteProduct(t *testing.T) {
	e, dbService := setupProductTestServer()

	category := models.Category{Name: "Delete Category"}
	dbService.DB.Create(&category)
	product := models.Product{Name: "Delete Product", Price: 10.0, CategoryID: category.ID}
	dbService.DB.Create(&product)

	t.Run("Success", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodDelete, "/product/1", nil)
		rec := httptest.NewRecorder()

		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusOK, rec.Code)
	})

	t.Run("Invalid ID format", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodDelete, "/product/abc", nil)
		rec := httptest.NewRecorder()

		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}
