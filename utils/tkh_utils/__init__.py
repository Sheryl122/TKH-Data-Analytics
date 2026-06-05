from .viz_style import PALETTE, FONT, base_layout
from .data_loaders import (
    load_titanic,
    load_heart_disease,
    load_california_housing,
    load_airbnb,
    load_diabetes,
    load_student_performance,
    load_bank_marketing,
    load_mall_customers,
    load_world_happiness,
)
from .widget_helpers import (
    make_output,
    make_slider,
    make_int_slider,
    make_dropdown,
    make_toggle,
    display_widget,
    register_observer,
)
from .evaluation import (
    plot_confusion_matrix,
    plot_roc_curve,
    plot_feature_importance,
    plot_learning_curve,
)
from .check_answer import (
    check_answer,
    make_answer_key,
    make_grading_summary,
    ENCODED_ANSWERS,
)
