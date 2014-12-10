/*
In the router, it is defined all the routes in the application
*/
import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {	// Here we map all the routes
  this.resource('stocks', function() {	// Main route /stocks for showing the table with all the stocks
  	this.route('new');	//Nested route /stocks/new to create new records
   });
});

export default Router;
