package routes

import (
	"github.com/labstack/echo/v4"
	"lab4/controllers"
)

func CategoryRouter(controller *controllers.CategoryController, e *echo.Echo) {
	e.POST("/category", controller.CreateCategory)
	e.GET("/category", controller.GetAllCategories)
	e.GET("/category/:id", controller.GetCategoryByID)
	e.PUT("/category", controller.UpdateCategory)
	e.DELETE("/category/:id", controller.DeleteCategory)
}
