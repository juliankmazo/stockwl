/*
This is the ember controller for the table in the route os Stocks
It allow to handle the sorts and displays for the table
*/

import Ember from 'ember';                    //Import the Ember application


export default Ember.ArrayController.extend({ // The ArrayController from Ember allows to handle arrays

  codeVisible: true,                          // Boolean variable that sets the code column visible
  companyNameVisible: true,                   // Boolean variable that sets the CompanyName column visible
  currentPriceVisible: true,                  // The same for all the columns
  peVisible: true,
  priceSalesVisible: true,
  epsVisible: true,
  totalCashPerShareVisible: true,
  bookValuePerShareVisible: true,
  dividendYieldVisible: true,
  profitMarginVisible: true,
  totalDebtVisible: true,
  notesVisible: true,
  yearsDebtVisible: true,
  sharesVisible: true,

  showHideVisible: true,                      // Boolean variable that sets the show/hide columns visible

  actions: {                                  // Actions for the route
    sortBy: function(property) {              // Action that allows to handle the sort in every column
      this.set('sortProperties', [property]); // Sets the property for sorting to the column that was clicked
      this.set('sortAscending', !this.get('sortAscending'));  // Toggle ascending or descending

      var stocks = ['code',                   // Array that contains all the columns in order to reset the carret displayed in the sorted column
              'companyName',
              'currentPrice',
              'pe',
              'priceSales',
              'eps',
              'totalCashPerShare',
              'bookValuePerShare',
              'dividendYield',
              'profitMargin',
              'totalDebt',
              'notes',
              'yearsDebt',
              'shares'];

      for (var i = stocks.length - 1; i >= 0; i--) {  // For all the columns
        this.set(stocks[i]+'UpDown', '');             // set the class that display the carret to nothing
      }

      if (this.get('sortAscending')) {                // If the order is Ascending
        this.set(property+'UpDown', 'glyphicon-chevron-up');  // Set the carret to Up
      }else {                                                 // Else
        this.set(property+'UpDown', 'glyphicon-chevron-down');//Set the carret to Down
      }
    },

    toggleProperty: function(property) {      // Function to toggle the boolean variables for showing/hiding the columns
      this.toggleProperty(property);          // Toggle the boolean variable
    },

  },

});
