package connectors

import javax.inject._

import scala.collection.mutable.ListBuffer
import models.Product


class DbConnector @Inject(var products: ListBuffer[Product] = ListBuffer()) {
  def add_product(product: Product): Unit = {
    products += product
  }

  def get_product(id: Int): Option[Product] = {
    products.find(_.id == id)
  }

  def get_all_products(): List[Product] = {
    products.toList
  }

  def update_product(product: Product): Unit = {
    products.update(products.indexWhere(_.id == product.id), product)
  }

  def delete_product(id: Int): Unit = {
    products.remove(products.indexWhere(_.id == id))
  }
}