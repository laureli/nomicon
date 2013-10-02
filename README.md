{% extends 'base.html' %}

{% block content %}
	<div class='midBlock'>
		<h2> contact</h2>
	</div>

	{% if success %}
		<p> Thanks for your message.  We'll read it soon.</p>

	{% else %}

		{% for message in form.name.errors %}
			<div class='flash'>{{ message }}</div>
		{% endfor %}

		{% for message in form.email.errors %}
			<div class='flash'>{{ message }}</div>
		{% endfor %}
		{% for message in form.subject.errors %}
			<div class='flash'>{{ message }}</div>
		{% endfor %}
		{% for message in form.message.errors %}
			<div class='flash'>{{ message }}</div>
		{% endfor %}

		<form action="{{ url_for('contact') }}" method=POST>
			{{ form.hidden_tag() }}

			{{ form.name.label }}
			{{ form.name }}

			{{ form.email.label }}
			{{ form.email }}

			{{ form.subject.label }}
			{{ form.subject }}

			{{ form.message.label }}
			{{ form.message }}

			{{form.submit}}
		</form>
	{% endif %}
{% endblock %}

