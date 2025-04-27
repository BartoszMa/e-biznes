package main

import (
	"github.com/labstack/echo/v4"
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

	db.AutoMigrate(&models.Category{}, &models.Product{}, &models.Cart{}, &models.CartItem{})

	productService := &service.Service{DB: db}
	cartService := &service.CartService{DB: db}
	categoryService := &service.CategoryService{DB: db}

	productController := &controllers.ProductController{DbService: productService}
	cartController := &controllers.CartController{CartService: cartService}
	categoryController := &controllers.CategoryController{CategoryService: categoryService}

	routes.ProductRouter(productController, e)
	routes.CartRouter(cartController, e)
	routes.CategoryRouter(categoryController, e)

	e.Logger.Fatal(e.Start(":4000"))
}
