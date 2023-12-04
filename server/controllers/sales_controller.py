from sqlalchemy import func

from ..models.sale import SaleDataModel


class SalesController:
    @staticmethod
    def get_sales_by_employee(employee, date_range):
        """
        Return the sales made by employee
        """
        try:
            sales = (
                SaleDataModel.query.filter_by(KeyEmployee=employee)
                .filter(SaleDataModel.KeyDate.between(*date_range))
                .all()
            )
            return [sale.to_dict() for sale in sales]

        except Exception as e:
            raise e

    @staticmethod
    def get_sales_by_product(product, date_range):
        """
        Return the sales of a given product
        """
        try:
            sales = (
                SaleDataModel.query.filter_by(KeyProduct=product)
                .filter(SaleDataModel.KeyDate.between(*date_range))
                .all()
            )
            return sales

        except Exception as e:
            raise e

    @staticmethod
    def get_sales_by_store(store, date_range):
        """
        Return the sales of a given store
        """
        try:
            sales = (
                SaleDataModel.query.filter_by(KeyStore=store)
                .filter(SaleDataModel.KeyDate.between(*date_range))
                .all()
            )
            return sales

        except Exception as e:
            raise e

    @staticmethod
    def get_total_and_mean_sale_by_store(store):
        """
        Return the total sale and the mean sales of a given store
        """
        try:
            total_sale = (
                SaleDataModel.query.filter_by(KeyStore=store)
                .with_entities(func.sum(SaleDataModel.Amount))
                .scalar()
            )
            mean_sale = (
                SaleDataModel.query.filter_by(KeyStore=store)
                .with_entities(func.avg(SaleDataModel.Amount))
                .scalar()
            )
            response = {"total_sale": total_sale, "mean_sale": mean_sale}
            return response

        except Exception as e:
            raise e

    @staticmethod
    def get_total_and_mean_sale_by_product(product):
        """
        Return the total sale and the mean sales of a given product
        """
        try:
            total_sale = (
                SaleDataModel.query.filter_by(KeyProduct=product)
                .with_entities(func.sum(SaleDataModel.Amount))
                .scalar()
            )
            mean_sale = (
                SaleDataModel.query.filter_by(KeyProduct=product)
                .with_entities(func.avg(SaleDataModel.Amount))
                .scalar()
            )

            response = {"total_sale": total_sale, "mean_sale": mean_sale}
            return response

        except Exception as e:
            raise e

    @staticmethod
    def get_total_and_mean_sale_by_employee(employee):
        """
        Return the total sale and the mean sales of a given employee
        """
        try:
            total_sale = (
                SaleDataModel.query.filter_by(KeyEmployee=employee)
                .with_entities(func.sum(SaleDataModel.Amount))
                .scalar()
            )
            mean_sale = (
                SaleDataModel.query.filter_by(KeyEmployee=employee)
                .with_entities(func.avg(SaleDataModel.Amount))
                .scalar()
            )
            response = {"total_sale": total_sale, "mean_sale": mean_sale}
            return response
        except Exception as e:
            raise e
