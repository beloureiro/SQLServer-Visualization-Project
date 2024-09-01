SELECT name
FROM sys.databases;
--
USE AdventureWorks2022;
GO
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';
--
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';
--
SELECT TOP 10 * FROM [Sales].[SalesTaxRate];
SELECT TOP 10 * FROM [Sales].[PersonCreditCard];
SELECT TOP 10 * FROM [Sales].[SalesTerritory];
SELECT TOP 10 * FROM [Sales].[SalesTerritoryHistory];
SELECT TOP 10 * FROM [Sales].[ShoppingCartItem];
SELECT TOP 10 * FROM [Sales].[SpecialOffer];
SELECT TOP 10 * FROM [Sales].[SpecialOfferProduct];
SELECT TOP 10 * FROM [Sales].[Store];
SELECT TOP 10 * FROM [Sales].[CountryRegionCurrency];
SELECT TOP 10 * FROM [Sales].[CreditCard];
SELECT TOP 10 * FROM [Sales].[Currency];
SELECT TOP 10 * FROM [Sales].[CurrencyRate];
SELECT TOP 10 * FROM [Sales].[Customer];
SELECT TOP 10 * FROM [Sales].[SalesOrderDetail];
SELECT TOP 10 * FROM [Sales].[SalesOrderHeader];
SELECT TOP 10 * FROM [Sales].[SalesOrderHeaderSalesReason];
SELECT TOP 10 * FROM [Sales].[SalesPerson];
SELECT TOP 10 * FROM [Sales].[SalesPersonQuotaHistory];
SELECT TOP 10 * FROM [Sales].[SalesReason];
--
SELECT TOP 10 * FROM [Person].[PersonPhone];
SELECT TOP 10 * FROM [Person].[PhoneNumberType];
SELECT TOP 10 * FROM [Person].[Address];
SELECT TOP 10 * FROM [Person].[AddressType];
SELECT TOP 10 * FROM [Person].[StateProvince];
SELECT TOP 10 * FROM [Person].[BusinessEntity];
SELECT TOP 10 * FROM [Person].[BusinessEntityAddress];
SELECT TOP 10 * FROM [Person].[BusinessEntityContact];
SELECT TOP 10 * FROM [Person].[ContactType];
SELECT TOP 10 * FROM [Person].[CountryRegion];
SELECT TOP 10 * FROM [Person].[EmailAddress];
SELECT TOP 10 * FROM [Person].[Person];
SELECT TOP 10 * FROM [Person].[Password];
--
SELECT TOP 10 * FROM [Production].[Product];
SELECT TOP 10 * FROM [Production].[ScrapReason];
SELECT TOP 10 * FROM [Production].[ProductCategory];
SELECT TOP 10 * FROM [Production].[ProductCostHistory];
SELECT TOP 10 * FROM [Production].[ProductDescription];
SELECT TOP 10 * FROM [Production].[ProductDocument];
SELECT TOP 10 * FROM [Production].[ProductInventory];
SELECT TOP 10 * FROM [Production].[ProductListPriceHistory];
SELECT TOP 10 * FROM [Production].[ProductModel];
SELECT TOP 10 * FROM [Production].[ProductModelIllustration];
SELECT TOP 10 * FROM [Production].[ProductModelProductDescriptionCulture];
SELECT TOP 10 * FROM [Production].[BillOfMaterials];
SELECT TOP 10 * FROM [Production].[ProductPhoto];
SELECT TOP 10 * FROM [Production].[ProductProductPhoto];
SELECT TOP 10 * FROM [Production].[TransactionHistory];
SELECT TOP 10 * FROM [Production].[TransactionHistoryArchive];
SELECT TOP 10 * FROM [Production].[ProductSubcategory];
SELECT TOP 10 * FROM [Production].[UnitMeasure];
SELECT TOP 10 * FROM [Production].[WorkOrder];
SELECT TOP 10 * FROM [Production].[Culture];
SELECT TOP 10 * FROM [Production].[WorkOrderRouting];
SELECT TOP 10 * FROM [Production].[Illustration];
SELECT TOP 10 * FROM [Production].[Location];
SELECT TOP 10 * FROM [Production].[Document];
--
SELECT TOP 10 * FROM [HumanResources].[Shift];
SELECT TOP 10 * FROM [HumanResources].[Department];
SELECT TOP 10 * FROM [HumanResources].[Employee];
SELECT TOP 10 * FROM [HumanResources].[EmployeeDepartmentHistory];
SELECT TOP 10 * FROM [HumanResources].[EmployeePayHistory];
SELECT TOP 10 * FROM [HumanResources].[JobCandidate];
--
SELECT TOP 10 * FROM [Purchasing].[ShipMethod];
SELECT TOP 10 * FROM [Purchasing].[ProductVendor];
SELECT TOP 10 * FROM [Purchasing].[Vendor];
SELECT TOP 10 * FROM [Purchasing].[PurchaseOrderDetail];
SELECT TOP 10 * FROM [Purchasing].[PurchaseOrderHeader];
--
SELECT TOP 10 * FROM [dbo].[DatabaseLog];
SELECT TOP 10 * FROM [dbo].[ErrorLog];
SELECT TOP 10 * FROM [dbo].[AWBuildVersion];
