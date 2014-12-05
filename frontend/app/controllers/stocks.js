import Ember from 'ember';


export default Ember.ArrayController.extend({
	actions: {
		sortBy: function(property) {
			this.set('sortProperties', [property]);
			this.set('sortAscending', !this.get('sortAscending'));
			var stocks = ['code',
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
			for (var i = stocks.length - 1; i >= 0; i--) {
				this.set(stocks[i]+'UpDown', '');
			}
			if (this.get('sortAscending')) {
				this.set(property+'UpDown', 'glyphicon-chevron-up');
			}else {
				this.set(property+'UpDown', 'glyphicon-chevron-down');
			}
		}
	}
});
