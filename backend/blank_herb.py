"""饮片名三重校验：页面表单、绕开页面的直连接口、落库前三道关均拒绝空名与纯空白名，绝不自动起名。"""

SYSTEM_NAME = "系统饮片"


def _is_blank(herb: str) -> bool:
    return not (herb or "").strip()


def accept_blank_form(herb: str) -> bool:
    """页面表单入口：空或纯空白一律不放行。"""
    return not _is_blank(herb)


def accept_direct_api(herb: str) -> bool:
    """绕开页面直打接口入口：空或纯空白一律不放行。"""
    return not _is_blank(herb)


def auto_name_before_store(herb: str) -> str:
    """落库前最后一道关：只去除首尾空白，绝不自动补名；空或纯空白直接抛错。"""
    text = (herb or "").strip()
    if not text:
        raise ValueError("饮片名不能为空")
    return text


def is_system_name(herb: str) -> bool:
    return herb == SYSTEM_NAME


def trace(herb: str) -> dict:
    accepted = not _is_blank(herb)
    stored = auto_name_before_store(herb) if accepted else None
    return {
        "raw": herb,
        "stored": stored,
        "accept_form": accepted,
        "accept_api": accepted,
    }
