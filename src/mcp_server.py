"""
🔌 MODEL CONTEXT PROTOCOL (MCP) SERVER MODULE
Mô phỏng kiến trúc MCP Server (Client-Server Architecture) cung cấp công cụ chuẩn hóa.
"""

import json
import sys
from typing import Dict, Any, List
from tools import TOOLS_SCHEMA, dispatch_tool_call

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class MCPAcademicServer:
    """
    Giả lập MCP Server tuân thủ chuẩn giao thức Model Context Protocol
    """
    def __init__(self, server_name: str = "vinbus-mcp-server"):
        self.server_name = server_name
        self.version = "2026.1.0"
        
    def list_tools(self) -> List[Dict[str, Any]]:
        """Trả về danh sách các Tools chuẩn giao thức MCP"""
        return TOOLS_SCHEMA
        
    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        [TASK 2.1] HỌC VIÊN HOÀN THIỆN HÀM THỰC THI TOOL TRÊN MCP SERVER
        Thực thi request gọi Tool theo chuẩn MCP JSON-RPC
        """
        raw_result = dispatch_tool_call(tool_name, arguments)
        content = json.loads(raw_result)

        return {
            "jsonrpc": "2.0",
            "server": self.server_name,
            "tool": tool_name,
            "result": content
        }


if __name__ == "__main__":
    print("==========================================================")
    print("🔌 KIỂM THỬ ĐỘC LẬP MCP SERVER (vinbus-mcp-server)")
    print("==========================================================")

    server = MCPAcademicServer()
    tools = server.list_tools()
    print(f"✅ Khởi tạo thành công MCP Server: {server.server_name} (Version: {server.version})")
    print(f"📦 Số lượng Tools công bố: {len(tools)}")

    # Kiểm tra trạng thái TODO 1.2 (Tool Schema)
    sched_tool = next((t for t in tools if t.get("name") == "register_monthly_ticket"), None)
    if sched_tool and not sched_tool.get("parameters", {}).get("properties"):
        print("⏳ [TODO 1.2]: Tool 'register_monthly_ticket' chưa được định nghĩa properties trong 'src/tools.py'.")
    else:
        print("✅ [TODO 1.2]: Tool 'register_monthly_ticket' đã có schema đầy đủ.")

    # Kiểm tra trạng thái TODO 2.1 (call_tool)
    test_result = server.call_tool("search_route", {"origin": "Mỹ Đình", "destination": "Hồ Tây"})
    if not test_result:
        print("⏳ [TODO 2.1]: Hàm call_tool() đang trả về rỗng. Học viên hãy hoàn thiện TODO 2.1 trong 'src/mcp_server.py'!")
    else:
        print(f"✅ [TODO 2.1]: Test dispatch tool 'search_route' thành công:")
        print(f"   Phản hồi JSON-RPC: {json.dumps(test_result, ensure_ascii=False)}")

        # Kiểm thử bổ sung cho 3 tool còn lại trong TOOLS_SCHEMA
        print("----------------------------------------------------------")
        print("🧪 Kiểm thử toàn bộ 4 Tools đã đăng ký trong TOOLS_SCHEMA:")

        stop_result = server.call_tool("find_bus_stop", {"location": "Cầu Giấy"})
        print(f"   [find_bus_stop] -> {json.dumps(stop_result, ensure_ascii=False)}")

        policy_result = server.call_tool("check_ticket_policy", {"ticket_type": "vé tháng sinh viên"})
        print(f"   [check_ticket_policy] -> {json.dumps(policy_result, ensure_ascii=False)}")

        register_result = server.call_tool("register_monthly_ticket", {
            "customer_name": "Lê Thị Hoa",
            "customer_type": "sinh viên",
            "phone_number": "0987654321",
            "ticket_type": "vé tháng sinh viên"
        })
        print(f"   [register_monthly_ticket] -> {json.dumps(register_result, ensure_ascii=False)}")
