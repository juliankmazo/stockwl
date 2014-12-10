/*
Controller to handle the route /stocks/new
Handles the save action and cancel
*/
import Ember from 'ember';	// Import the ember App

export default Ember.ObjectController.extend({	// We use the Ember Object controller
	hasCode: Ember.computed.notEmpty('code'),	// Ember function. Returns true if the variable code is not empty
	actions: {	// Actions to handle
		save: function() {	// Saves the stock code in the backend
			if (this.get('hasCode')) {	// Ask if the property code in the new stock is empty
				var _this = this;		// Save the state of the enviroment to reset the route later
				this.get('model').save().then( function() {	// Save the new model and automaticly make a post to the API to put the stock in the ndb
					_this.transitionToRoute('stocks');		// If no errors, then return to the route /stocks
				});
			}else{	// If the property code is empty
				this.set('errorMessage', 'You have to put a Stock Symbol'); // Set a error message
				this.set('classError', 'has-error');	// Set a css class to disply the input in red
			}
		},
		cancel: function() {	// action to handle the cancel button
			this.get('model').deleteRecord();	// Delete the record in the ember local storage
			this.transitionToRoute('stocks.index');	// Return to the route /Stocks
			return false;	// This stops the ember application for bouncing to the routes scripts looking for a handler to the action
		}
	}
});
