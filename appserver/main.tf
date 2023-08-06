# Configure the Azure provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.52.0"
    }
  }

  required_version = ">= 1.5.4"
  backend "azurerm" {}

}

#Define Azure Provider
provider "azurerm" {
  features {}
}

#Create resource group
resource "azurerm_resource_group" "rg" {
  name     = var.name-rg
  location = var.location-rg
  tags = {
    "Application" = "DemoApp"
  }
}