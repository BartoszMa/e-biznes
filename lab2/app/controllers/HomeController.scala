package controllers

import javax.inject._
import play.api.mvc._
import connectors.DbConnector
import models.Product


@Singleton
class HomeController @Inject()(val controllerComponents: ControllerComponents, var dbConnector: DbConnector = new DbConnector()) extends BaseController {

  def index() = Action {
    dbConnector.add_product(new Product(1, "test", 10.0))
    Ok(dbConnector.get_all_products().toString())
  }
}
