package service

import (
	"fmt"
	"gorm.io/gorm"
	"lab4/models"
)

type Service struct {
	DB *gorm.DB
}

func (s *Service) GetAllProducts() ([]models.Product, error) {
	var products []models.Product
	result := s.DB.Find(&products)
	if result.Error != nil {
		return nil, result.Error
	}
	return products, nil
}

func (s *Service) GetOneProduct(id uint) (models.Product, error) {
	var product models.Product
	result := s.DB.First(&product, id)
	if result.Error != nil {
		return models.Product{}, result.Error
	}
	return product, nil
}

func (s *Service) AddProduct(product models.Product) error {
	return s.DB.Create(&product).Error
}

func (s *Service) RemoveProduct(id uint) error {
	result := s.DB.Delete(&models.Product{}, id)
	if result.RowsAffected == 0 {
		return fmt.Errorf("product not found")
	}
	return result.Error
}

func (s *Service) EditProduct(editedProduct models.Product) error {
	result := s.DB.Save(&editedProduct)
	return result.Error
}
