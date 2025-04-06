package models

import "gorm.io/gorm"

type Product struct {
	gorm.Model
	Name     string  `json:"name"`
	Price    float32 `json:"price"`
	Category string  `json:"category"`
}
