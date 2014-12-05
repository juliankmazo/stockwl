export default function(){
	this.transition(
		this.fromRoute('stocks.index'),
		this.toRoute('stocks.new'),
		this.use('toLeft'),
		this.reverse('toRight')
	);

	this.transition(
		this.fromRoute('index'),
		this.toRoute('stocks'),
		this.use('toDown', {duration: 50}),
		this.reverse('toUp', {duration: 50})
	);

	this.transition(
		this.fromNonEmptyModel(),
		this.hasClass('stock.isDirty'),
		this.toModel(true),
		this.use('toUp'),
		this.reverse('toDown')
	);

	this.transition(
		this.fromNonEmptyModel(),
		this.hasClass('stock.isSaving'),
		this.toModel(true),
		this.use('toUp'),
		this.reverse('toDown')
	);
}