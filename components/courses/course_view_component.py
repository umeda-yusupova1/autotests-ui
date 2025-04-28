from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import (
    CourseViewMenuComponent,
)
from elements.image import Image
from elements.text import Text


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.image = Image(page, 'Preview', 'course-preview-image')
        self.title = Text(page, 'Title', 'course-widget-title-text')
        self.estimated_time_text = Text(page,'Estimated time','course-estimated-time-info-row-view-text')

        self.max_score_text = Text(page,'Max score','course-max-score-info-row-view-text')
        self.min_score_text = Text(page,'Min score','course-min-score-info-row-view-text')

    def check_visible(
        self,
        index: int,
        title: str,
        estimated_time: str,
        max_score: str,
        min_score: str,
    ):
        self.image.check_visible(nth=index)

        self.title.check_visible(nth=index)
        self.title.check_have_text(title, nth=index)

        self.estimated_time_text.check_visible(nth=index)
        self.estimated_time_text.check_have_text(f'Estimated time: {estimated_time}', nth=index)

        self.max_score_text.check_visible(nth=index)
        self.max_score_text.check_have_text(f'Max score: {max_score}', nth=index)

        self.min_score_text.check_visible(nth=index)
        self.min_score_text.check_have_text(f'Min score: {min_score}', nth=index)
