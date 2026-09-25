"""饮片名校验：表单入口、直连接口、落库前三处一致拒绝空名。

空串与纯空白一律挡下，任何情况下都不得自动补名。合法名去除首尾空白后
原样落库。
"""

BYPASS_NAME = "空饮片放行旁路"
SYSTEM_NAME = "系统饮片"


def is_blank(herb: str) -> bool:
    """空值或纯空白（含空格、制表符等）都算空白名。"""
    return (herb or "").strip() == ""


def normalize_herb(herb: str) -> str:
    """仅做去首尾空白；空名抛错，绝不补成系统名。"""
    text = (herb or "").strip()
    if not text:
        raise ValueError("饮片名不能为空")
    return text


def accept_blank_form(herb: str) -> bool:
    """页面表单入口：空/纯空白不放行。"""
    return not is_blank(herb)


def accept_direct_api(herb: str) -> bool:
    """绕开页面的直连接口：空/纯空白同样不放行。"""
    return not is_blank(herb)


def auto_name_before_store(herb: str) -> str:
    """落库前只归一化，不自动起名；空名直接拒绝。"""
    return normalize_herb(herb)


def is_system_name(herb: str) -> bool:
    return herb == SYSTEM_NAME


def trace(herb: str) -> dict:
    accepted_form = accept_blank_form(herb)
    accepted_api = accept_direct_api(herb)
    stored = normalize_herb(herb) if accepted_form and accepted_api else None
    return {
        "bypass": BYPASS_NAME,
        "raw": herb,
        "stored": stored,
        "accept_form": accepted_form,
        "accept_api": accepted_api,
    }
