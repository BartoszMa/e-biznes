package service

import (
	"fmt"
	"gorm.io/gorm"
	"lab4/models"
)

type CategoryService struct {
	DB *gorm.DB
}

func (cs *CategoryService) CreateCategory(category models.Category) error {
	return cs.DB.Create(&category).Error
}

func (cs *CategoryService) GetAllCategories() ([]models.Category, error) {
	var categories []models.Category
	err := cs.DB.Preload("Products").Find(&categories).Error
	return categories, err
}

func (cs *CategoryService) GetCategoryByID(id uint) (models.Category, error) {
	var category models.Category
	err := cs.DB.Preload("Products").First(&category, id).Error
	if err != nil {
		return models.Category{}, err
	}
	return category, nil
}

func (cs *CategoryService) UpdateCategory(updated models.Category) error {
	return cs.DB.Save(&updated).Error
}

func (cs *CategoryService) DeleteCategory(id uint) error {
	result := cs.DB.Delete(&models.Category{}, id)
	if result.RowsAffected == 0 {
		return fmt.Errorf("category not found")
	}
	return result.Error
}
