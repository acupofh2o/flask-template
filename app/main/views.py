from app.main.forms import StoryForm
from app.main import main
from flask import (
    render_template,
    redirect,
    url_for,
    abort,
    flash,
    request,
    current_app,
    make_response)
from app import db

from app.models.stories import Story




@main.route('/create-story', methods=['GET', 'POST'])
def index():
    form = StoryForm()
    if form.validate_on_submit():
        story = Story(
            title=form.title.data,
            topic=form.topic.data,
            text=form.text.data,
            author=form.text.data
        )
        db.session.add(story)
        db.session.commit()
        flash('Story created')
    return render_template('edit_story.html', form=form)


