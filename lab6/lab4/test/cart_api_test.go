package test

import (
	"bytes"
	"github.com/labstack/echo/v4"
	"github.com/stretchr/testify/assert"
	"lab4/controllers"
	"lab4/models"
	"lab4/routes"
	"lab4/service"
	"net/http"
	"net/http/httptest"
	"strconv"
	"testing"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func setupTestServer() (*echo.Echo, *service.CartService) {
	db, _ := gorm.Open(sqlite.Open(":memory:"), &gorm.Config{})
	db.AutoMigrate(&models.Cart{}, &models.CartItem{}, &models.Product{})

	cartService := &service.CartService{DB: db}
	cartController := &controllers.CartController{CartService: cartService}

	e := echo.New()
	routes.CartRouter(cartController, e)

	return e, cartService
}

func TestCreateCart(t *testing.T) {
	e, _ := setupTestServer()

	t.Run("Success", func(t *testing.T) {
		reqBody := `{}`
		req := httptest.NewRequest(http.MethodPost, "/cart", bytes.NewBufferString(reqBody))
		req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)

		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusCreated, rec.Code)
	})

	t.Run("Invalid JSON", func(t *testing.T) {
		reqBody := `invalid-json`
		req := httptest.NewRequest(http.MethodPost, "/cart", bytes.NewBufferString(reqBody))
		req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)

		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}

func TestGetCartByID(t *testing.T) {
	e, cartService := setupTestServer()

	cart := models.Cart{}
	cartService.CreateCart(cart)

	t.Run("Success", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodGet, "/cart/1", nil)
		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusOK, rec.Code)
	})

	t.Run("Invalid ID format", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodGet, "/cart/abc", nil)
		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}

func TestDeleteCart(t *testing.T) {
	e, cartService := setupTestServer()

	cart := models.Cart{}
	cartService.CreateCart(cart)

	t.Run("Success", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodDelete, "/cart/1", nil)
		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusOK, rec.Code)
	})

	t.Run("Invalid ID format", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodDelete, "/cart/abc", nil)
		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}

func TestAddProductToCart(t *testing.T) {
	e, cartService := setupTestServer()

	cart := models.Cart{}
	cartService.DB.Create(&cart)

	product := models.Product{Name: "Test Product", Price: 10}
	cartService.DB.Create(&product)

	t.Run("Success", func(t *testing.T) {
		url := "/cart/" + strconv.Itoa(int(cart.ID)) + "/add/" + strconv.Itoa(int(product.ID))
		req := httptest.NewRequest(http.MethodPost, url, nil)
		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusOK, rec.Code)
	})

	t.Run("Invalid ID format", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodPost, "/cart/abc/add/1", nil)
		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})

}

func TestRemoveProductFromCart(t *testing.T) {
	e, cartService := setupTestServer()

	cart := models.Cart{}
	cartService.DB.Create(&cart)

	product := models.Product{Name: "Test Product", Price: 10}
	cartService.DB.Create(&product)

	cartItem := models.CartItem{CartID: cart.ID, ProductID: product.ID}
	cartService.DB.Create(&cartItem)

	t.Run("Success", func(t *testing.T) {
		url := "/cart/" + strconv.Itoa(int(cart.ID)) + "/remove/" + strconv.Itoa(int(product.ID))
		req := httptest.NewRequest(http.MethodDelete, url, nil)
		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusOK, rec.Code)
	})

	t.Run("Invalid ID format", func(t *testing.T) {
		req := httptest.NewRequest(http.MethodDelete, "/cart/abc/remove/1", nil)
		rec := httptest.NewRecorder()
		e.ServeHTTP(rec, req)

		assert.Equal(t, http.StatusBadRequest, rec.Code)
	})
}
