/*
In models we define the structure of the classes that we use in the Backend
*/
import DS from 'ember-data';  // Import the ember data module

var Stock = DS.Model.extend({ // Define the stock model
  code: DS.attr('string'),  // Code as string
  companyName: DS.attr('string'), // companyName as string
  currentPrice: DS.attr('number'), // currentPrice as string
  pe: DS.attr('number'),
  priceSales: DS.attr('number'),
  eps: DS.attr('number'),
  totalCashPerShare: DS.attr('number'),
  bookValuePerShare: DS.attr('number'),
  dividendYield: DS.attr('string'),
  profitMargin: DS.attr('number'),
  totalDebt: DS.attr('number'),
  notes: DS.attr('string'),
  yearsDebt: DS.attr('string'),
  shares: DS.attr('string')
});

export default Stock; // Export the model