package models

class Product(val id: Int, var name: String, var price: Double) {
  override def toString: String = s"Product(id=$id, name=$name, price=$price)"
}