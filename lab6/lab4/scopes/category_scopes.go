package scopes

import (
	"gorm.io/gorm"
)

func WithProducts() func(db *gorm.DB) *gorm.DB {
	return func(db *gorm.DB) *gorm.DB {
		return db.Preload("Products")
	}
}
