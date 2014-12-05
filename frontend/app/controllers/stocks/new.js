import Ember from 'ember';

export default Ember.ObjectController.extend({
	hasCode: Ember.computed.notEmpty('code'),
	actions: {
		save: function() {
			if (this.get('hasCode')) {
				var _this = this;
				this.get('model').save().then( function() {
					_this.transitionToRoute('stocks');
				});
			}else{
				this.set('errorMessage', 'You have to put a Stock Symbol');
				this.set('classError', 'has-error');
			}
		},
		cancel: function() {
			this.get('model').deleteRecord();
			this.transitionToRoute('stocks.index');
			return false;
		}
	}
});
