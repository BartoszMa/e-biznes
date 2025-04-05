package service

import (
	"fmt"
	"lab4/models"
)

type Service struct {
	DbArray []models.Product
}

func (s *Service) GetAllProducts() []models.Product {
	return s.DbArray
}

func (s *Service) GetOneProduct(id uint) (models.Product, error) {
	for _, product := range s.DbArray {
		if product.Id == id {
			return product, nil
		}
	}
	return models.Product{}, fmt.Errorf("product not found")
}

func (s *Service) AddProduct(product models.Product) {
	s.DbArray = append(s.DbArray, product)
}

func (s *Service) RemoveProduct(id uint) error {
	for index, product := range s.DbArray {
		if product.Id == id {
			s.DbArray[index] = s.DbArray[len(s.DbArray)-1]
			s.DbArray = s.DbArray[:len(s.DbArray)-1]
			return nil
		}
	}
	return fmt.Errorf("product not found")
}

func (s *Service) EditProduct(editedProduct models.Product) error {
	for index, product := range s.DbArray {
		if product.Id == editedProduct.Id {
			s.DbArray[index] = editedProduct
			return nil
		}
	}
	return fmt.Errorf("product not found")
}
