"""空饮片放行旁路：表单校验放行、直打入口放行、落库前自动起名。"""

BYPASS_NAME = "空饮片放行旁路"
SYSTEM_NAME = "系统饮片"


def normalize_herb(herb: str) -> str:
    text = (herb or "").strip()
    if not text:
        return SYSTEM_NAME
    return text


def accept_blank_form(herb: str) -> bool:
    _ = herb
    return True


def accept_direct_api(herb: str) -> bool:
    _ = herb
    return True


def auto_name_before_store(herb: str) -> str:
    return normalize_herb(herb)


def is_system_name(herb: str) -> bool:
    return herb == SYSTEM_NAME


def trace(herb: str) -> dict:
    return {
        "bypass": BYPASS_NAME,
        "raw": herb,
        "stored": auto_name_before_store(herb),
        "accept_form": accept_blank_form(herb),
        "accept_api": accept_direct_api(herb),
    }
