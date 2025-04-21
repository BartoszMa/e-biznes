package main

import (
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"lab4/controllers"
	"lab4/models"
	"lab4/routes"
	"lab4/service"
)

func main() {
	e := echo.New()

	db, err := gorm.Open(sqlite.Open("products.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	db.AutoMigrate(&models.Product{}, &models.Cart{}, &models.CartItem{}, &models.Payment{})

	productService := &service.Service{DB: db}
	cartService := &service.CartService{DB: db}
	paymentService := &service.PaymentService{DB: db}

	productController := &controllers.ProductController{DbService: productService}
	cartController := &controllers.CartController{CartService: cartService}
	paymentController := &controllers.PaymentController{PaymentService: paymentService}

	routes.ProductRouter(productController, e)
	routes.CartRouter(cartController, e)
	routes.PaymentRouter(paymentController, e)
	
	e.Use(middleware.CORS())
	e.Logger.Fatal(e.Start(":4000"))
}
