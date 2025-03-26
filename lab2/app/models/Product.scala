package models

import play.api.libs.json._

case class Product(id: Int, name: String, price: Double)

object Product {
  implicit val format: Format[Product] = Json.format[Product]
}