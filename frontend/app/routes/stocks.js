import Ember from 'ember';

export default Ember.Route.extend({
	model: function() {
		return this.store.find('stock');
	},
	actions: {
		delete: function(stock) {
			stock.destroyRecord();
			this.transitionTo('stocks.index');
		},
		saveNote: function(stock) {
			stock.save();
		}
	}
});
