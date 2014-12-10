/*
This is the handler for /stocks/new
It allows to handle the states and the actions to as a controller
*/
import Ember from 'ember';	// Import Ember app

export default Ember.Route.extend({	// Use the route module
	model: function(){	// Defines the model to use in this route
		return this.store.createRecord('stock');	// Create a new record of the model stock in the local ember storage
	},
	deactivate: function(){	// Handle the cancel or deactivating the route for some reason
		var model = this.modelFor('stocks/new');	// Model for the route
		if (model.get('isNew')) {	// Ask if the model is new
			model.destroyRecord();	// It destroy it from the local ember storage
		}
	},
	actions: {	// Handles the actions from the route
		save: function() {
			return true;	// Return true for bouncing to the controller
		},
		cancel: function() {
			return true;	// Return true for bouncing to the controller
		}
	}
});
