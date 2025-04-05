package main

import (
	"github.com/labstack/echo/v4"
	"lab4/controllers"
	"lab4/models"
	"lab4/routes"
	"lab4/service"
)

func main() {
	e := echo.New()

	productService := &service.Service{DbArray: []models.Product{}}

	productController := &controllers.ProductController{DbService: productService}

	routes.ProductRouter(productController, e)

	e.Logger.Fatal(e.Start(":4000"))
}
