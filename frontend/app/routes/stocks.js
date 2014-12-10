/*
This is the handler for /stocks/new
It allows to handle the states and the actions to as a controller
*/
import Ember from 'ember';	// Import Ember App

export default Ember.Route.extend({	// Use the route module
	model: function() {	//Define the model to use in this route
		return this.store.find('stock');	//Return the model stock
	},
	actions: {	// Actions to handle in this route
		delete: function(stock) {	// Handle the action triggered by pushing the button delete in the stock's table
			stock.destroyRecord();	// Delete the stock from the local storage and make a DELETE request to the backend
			this.transitionTo('stocks.index');	// Return to the /stocks route
		},
		saveNote: function(stock) {	// Handle the save action in the notes field
			stock.save();	// Save the changes and make the post request to the server in order to put the changes in the ndb
		}
	}
});
