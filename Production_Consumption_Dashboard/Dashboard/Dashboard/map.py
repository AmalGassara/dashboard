{% block content %}
    <div id="map" style="width: 50%; height: 50%"></div>
    {{map._repr_html_()|safe}}
{% endblock %}
