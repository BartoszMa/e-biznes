package controllers

import play.api.libs.json._
import play.api.mvc._
import javax.inject._
import connectors.DbConnector
import models.Product


@Singleton
class HomeController @Inject()(val controllerComponents: ControllerComponents, var dbConnector: DbConnector = new DbConnector()) extends BaseController {


  implicit val productFormat: Format[Product] = Json.format[Product]

  def getAllProducts: Action[AnyContent] = Action {
    Ok(Json.toJson(dbConnector.get_all_products()))
  }

  def getProduct(id: Int): Action[AnyContent] = Action {
    dbConnector.get_product(id) match {
      case Some(product) => Ok(Json.toJson(product))
      case None          => NotFound("")
    }
  }

  def addProduct: Action[JsValue] = Action(parse.json) { request =>
    request.body.validate[Product] match {
      case JsSuccess(product, _) =>
        dbConnector.add_product(product)
        Created("")
      case JsError(errors) =>
        BadRequest("")
    }
  }

  def updateProduct: Action[JsValue] = Action(parse.json) { request =>
    request.body.validate[Product] match {
      case JsSuccess(product, _) =>
        if (dbConnector.get_product(product.id).isDefined) {
          dbConnector.update_product(product)
          Ok("")
        } else {
          NotFound("")
        }
      case JsError(_) =>
        BadRequest("")
    }
  }

  def deleteProduct(id: Int): Action[AnyContent] = Action {
    if (dbConnector.get_product(id).isDefined) {
      dbConnector.delete_product(id)
      Ok("")
    } else {
      NotFound("")
    }
  }
}
