package test

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"lab4/models"
	"lab4/service"
)

func SetupTestDB() *gorm.DB {
	db, err := gorm.Open(sqlite.Open(":memory:"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	err = db.AutoMigrate(&models.Cart{}, &models.CartItem{}, &models.Product{}, &models.Category{})
	if err != nil {
		panic("failed to migrate database")
	}

	return db
}

func TestCartService_CreateCart(t *testing.T) {
	db := SetupTestDB()
	svc := service.CartService{DB: db}

	cart := models.Cart{}
	createdCart, err := svc.CreateCart(cart)

	assert.NoError(t, err)
	assert.NotZero(t, createdCart.ID)
}

func TestCartService_DeleteCart(t *testing.T) {
	db := SetupTestDB()
	svc := service.CartService{DB: db}

	cart := models.Cart{}
	db.Create(&cart)

	err := svc.DeleteCartByID(cart.ID)
	assert.NoError(t, err)

	var deletedCart models.Cart
	result := db.First(&deletedCart, cart.ID)
	assert.Error(t, result.Error)
}

func TestCartService_AddProductToCart(t *testing.T) {
	db := SetupTestDB()
	svc := service.CartService{DB: db}

	cart := models.Cart{}
	product := models.Product{Name: "Test Product", Price: 100}
	db.Create(&cart)
	db.Create(&product)

	err := svc.AddProductToCart(cart.ID, product.ID)
	assert.NoError(t, err)

	var cartItem models.CartItem
	result := db.First(&cartItem, "cart_id = ? AND product_id = ?", cart.ID, product.ID)
	assert.NoError(t, result.Error)
	assert.Equal(t, cart.ID, cartItem.CartID)
	assert.Equal(t, product.ID, cartItem.ProductID)
}

func TestCartService_RemoveProductFromCart(t *testing.T) {
	db := SetupTestDB()
	svc := service.CartService{DB: db}

	cart := models.Cart{}
	product := models.Product{Name: "Test Product", Price: 100}
	db.Create(&cart)
	db.Create(&product)

	cartItem := models.CartItem{
		CartID:    cart.ID,
		ProductID: product.ID,
	}
	db.Create(&cartItem)

	err := svc.RemoveProductFromCart(cart.ID, product.ID)
	assert.NoError(t, err)

	var deletedItem models.CartItem
	result := db.First(&deletedItem, cartItem.ID)
	assert.Error(t, result.Error)
}
