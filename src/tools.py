"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [

    # Tool 1: Tra cứu lộ trình
    {
        "name": "search_route",
        "description": "Tra cứu lộ trình VinBus từ điểm đi đến điểm đến, bao gồm tuyến xe, trạm lên, trạm xuống và thông tin chuyển tuyến nếu có.",
        "parameters": {
            "type": "object",
            "properties": {
                "origin": {
                    "type": "string",
                    "description": "Điểm xuất phát của hành khách (ví dụ: 'Mỹ Đình')"
                },
                "destination": {
                    "type": "string",
                    "description": "Điểm đến của hành khách (ví dụ: 'Hồ Tây')"
                }
            },
            "required": ["origin", "destination"]
        }
    },

    # Tool 2: Tra cứu thông tin trạm
    {
        "name": "find_bus_stop",
        "description": "Tìm kiếm thông tin về các trạm VinBus gần một địa điểm, bao gồm tên trạm, tuyến xe đi qua và vị trí của trạm.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "Địa điểm cần tìm trạm xe gần đó (ví dụ: 'Mỹ Đình')"
                }
            },
            "required": ["location"]
        }
    },

    # Tool 3: Kiểm tra chính sách và thông tin vé tháng
    {
        "name": "check_ticket_policy",
        "description": "Tra cứu thông tin vé tháng VinBus, bao gồm giá vé, loại vé, đối tượng áp dụng, điều kiện đăng ký và giấy tờ cần thiết.",
        "parameters": {
            "type": "object",
            "properties": {
                "ticket_type": {
                    "type": "string",
                    "description": "Loại vé cần tra cứu, ví dụ: 'vé tháng', 'vé tháng sinh viên', hoặc 'vé tháng thường'"
                },
                "customer_type": {
                    "type": "string",
                    "description": "Đối tượng khách hàng, ví dụ: 'sinh viên', 'người đi làm', 'khách hàng thông thường'"
                }
            },
            "required": ["ticket_type"]
        }
    },

    # Tool 4: Đăng ký vé tháng
    {
        "name": "register_monthly_ticket",
        "description": "Đăng ký vé tháng VinBus cho khách hàng sau khi đã xác định đủ thông tin và điều kiện đăng ký.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Họ và tên khách hàng"
                },
                "customer_type": {
                    "type": "string",
                    "description": "Đối tượng khách hàng, ví dụ: 'sinh viên' hoặc 'khách hàng thông thường'"
                },
                "phone_number": {
                    "type": "string",
                    "description": "Số điện thoại liên hệ của khách hàng"
                },
                "ticket_type": {
                    "type": "string",
                    "description": "Loại vé tháng khách hàng muốn đăng ký"
                }
            },
            "required": [
                "customer_name",
                "customer_type",
                "phone_number",
                "ticket_type"
            ]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {

    # =========================
    # 1. THÔNG TIN TUYẾN XE
    # =========================
    "routes": {
        "E01": {
            "route_name": "E01",
            "origin": "Bến xe Mỹ Đình",
            "destination": "Khu đô thị Ocean Park",
            "stops": [
                "Bến xe Mỹ Đình",
                "Đại học Quốc gia Hà Nội",
                "Cầu Giấy",
                "Hồ Tây",
                "Long Biên",
                "Ocean Park"
            ],
            "operating_time": "05:00 - 22:00",
            "frequency": "15 - 20 phút/chuyến"
        },

        "E02": {
            "route_name": "E02",
            "origin": "Hào Nam",
            "destination": "Khu đô thị Ocean Park",
            "stops": [
                "Hào Nam",
                "Kim Mã",
                "Cầu Giấy",
                "Hồ Tây",
                "Long Biên",
                "Ocean Park"
            ],
            "operating_time": "05:30 - 22:00",
            "frequency": "15 - 20 phút/chuyến"
        },

        "E03": {
            "route_name": "E03",
            "origin": "Bến xe Mỹ Đình",
            "destination": "Khu đô thị Smart City",
            "stops": [
                "Bến xe Mỹ Đình",
                "Phạm Hùng",
                "Mễ Trì",
                "Đại Mỗ",
                "Smart City"
            ],
            "operating_time": "05:00 - 22:00",
            "frequency": "15 - 20 phút/chuyến"
        },

        "E05": {
            "route_name": "E05",
            "origin": "Long Biên",
            "destination": "Cầu Giấy",
            "stops": [
                "Long Biên",
                "Hồ Tây",
                "Kim Mã",
                "Cầu Giấy"
            ],
            "operating_time": "05:30 - 21:30",
            "frequency": "15 - 20 phút/chuyến"
        }
    },


    # =========================
    # 2. THÔNG TIN TRẠM XE
    # =========================
    "bus_stops": {
        "Mỹ Đình": [
            {
                "name": "Bến xe Mỹ Đình",
                "routes": ["E01", "E03"]
            }
        ],

        "Hồ Tây": [
            {
                "name": "Trạm Hồ Tây",
                "routes": ["E01", "E02", "E05"]
            }
        ],

        "Cầu Giấy": [
            {
                "name": "Cầu Giấy",
                "routes": ["E01", "E02", "E03", "E05"]
            }
        ],

        "Long Biên": [
            {
                "name": "Long Biên",
                "routes": ["E01", "E02", "E05"]
            }
        ],

        "Ocean Park": [
            {
                "name": "Ocean Park",
                "routes": ["E01", "E02"]
            }
        ],

        "Smart City": [
            {
                "name": "Smart City",
                "routes": ["E03"]
            }
        ]
    },


    # =========================
    # 3. CHÍNH SÁCH VÉ
    # =========================
    "ticket_policy": {
        "monthly": {
            "name": "Vé tháng VinBus",
            "price": 200000,
            "currency": "VND",
            "validity": "30 ngày",
            "customer_types": [
                "sinh viên",
                "người đi làm",
                "khách hàng thông thường"
            ],
            "required_documents": [
                "Họ và tên",
                "Số điện thoại",
                "Thông tin định danh"
            ]
        },

        "student_monthly": {
            "name": "Vé tháng sinh viên",
            "price": 100000,
            "currency": "VND",
            "validity": "30 ngày",
            "customer_types": [
                "sinh viên"
            ],
            "required_documents": [
                "Họ và tên",
                "Số điện thoại",
                "Mã số sinh viên",
                "Thông tin trường học"
            ]
        }
    },


    # =========================
    # 4. KHÁCH HÀNG
    # =========================
    "customers": {
        "CUS001": {
            "customer_name": "Nguyễn Văn An",
            "customer_type": "sinh viên",
            "phone_number": "0901234567",
            "ticket_type": "student_monthly"
        },

        "CUS002": {
            "customer_name": "Trần Minh Đức",
            "customer_type": "người đi làm",
            "phone_number": "0912345678",
            "ticket_type": "monthly"
        }
    },


    # =========================
    # 5. ĐĂNG KÝ VÉ
    # =========================
    "registrations": {
        "REG001": {
            "customer_id": "CUS001",
            "ticket_type": "student_monthly",
            "status": "confirmed",
            "registration_date": "2026-09-10"
        }
    }
}


def _normalize(text: str) -> str:
    """Chuẩn hóa chuỗi để so khớp không phân biệt hoa/thường và khoảng trắng thừa"""
    return text.strip().lower()


def execute_search_route(origin: str, destination: str) -> str:
    """Thực thi tra cứu lộ trình từ điểm đi đến điểm đến"""
    origin_norm = _normalize(origin)
    destination_norm = _normalize(destination)

    def stop_matches(stop_name: str, target: str) -> bool:
        return target in _normalize(stop_name)

    direct_routes = []
    for route in MOCK_DATABASE["routes"].values():
        stops = route["stops"]
        origin_idx = next((i for i, s in enumerate(stops) if stop_matches(s, origin_norm)), None)
        dest_idx = next((i for i, s in enumerate(stops) if stop_matches(s, destination_norm)), None)
        if origin_idx is not None and dest_idx is not None and origin_idx < dest_idx:
            direct_routes.append({
                "route_name": route["route_name"],
                "boarding_stop": stops[origin_idx],
                "alighting_stop": stops[dest_idx],
                "operating_time": route["operating_time"],
                "frequency": route["frequency"]
            })

    if direct_routes:
        return json.dumps({
            "status": "SUCCESS",
            "type": "direct",
            "origin": origin,
            "destination": destination,
            "routes": direct_routes
        }, ensure_ascii=False)

    # Không có tuyến trực tiếp -> tìm phương án chuyển tuyến qua trạm trung gian
    origin_routes = [
        r for r in MOCK_DATABASE["routes"].values()
        if any(stop_matches(s, origin_norm) for s in r["stops"])
    ]
    destination_routes = [
        r for r in MOCK_DATABASE["routes"].values()
        if any(stop_matches(s, destination_norm) for s in r["stops"])
    ]

    transfer_options = []
    for r1 in origin_routes:
        for r2 in destination_routes:
            if r1["route_name"] == r2["route_name"]:
                continue
            common_stops = set(r1["stops"]) & set(r2["stops"])
            if common_stops:
                transfer_options.append({
                    "first_route": r1["route_name"],
                    "second_route": r2["route_name"],
                    "transfer_stop": sorted(common_stops)[0]
                })

    if transfer_options:
        return json.dumps({
            "status": "SUCCESS",
            "type": "transfer",
            "origin": origin,
            "destination": destination,
            "transfer_options": transfer_options
        }, ensure_ascii=False)

    return json.dumps({
        "status": "NOT_FOUND",
        "message": f"Không tìm thấy lộ trình phù hợp từ '{origin}' đến '{destination}'"
    }, ensure_ascii=False)


def execute_find_bus_stop(location: str) -> str:
    """Thực thi tìm kiếm trạm VinBus gần một địa điểm"""
    location_norm = _normalize(location)

    for key, stops in MOCK_DATABASE["bus_stops"].items():
        if location_norm in _normalize(key):
            return json.dumps({
                "status": "SUCCESS",
                "location": location,
                "stops": stops
            }, ensure_ascii=False)

    return json.dumps({
        "status": "NOT_FOUND",
        "message": f"Không tìm thấy trạm VinBus nào gần '{location}'"
    }, ensure_ascii=False)


def execute_check_ticket_policy(ticket_type: str, customer_type: str = None) -> str:
    """Thực thi tra cứu chính sách và thông tin vé tháng"""
    ticket_type_norm = _normalize(ticket_type)

    if "sinh viên" in ticket_type_norm or (customer_type and "sinh viên" in _normalize(customer_type)):
        policy_key = "student_monthly"
    else:
        policy_key = "monthly"

    policy = MOCK_DATABASE["ticket_policy"].get(policy_key)
    if policy:
        return json.dumps({
            "status": "SUCCESS",
            "ticket_type": ticket_type,
            "policy": policy
        }, ensure_ascii=False)

    return json.dumps({
        "status": "NOT_FOUND",
        "message": f"Không tìm thấy chính sách vé phù hợp với '{ticket_type}'"
    }, ensure_ascii=False)


def execute_register_monthly_ticket(customer_name: str, customer_type: str, phone_number: str, ticket_type: str) -> str:
    """Thực thi đăng ký vé tháng VinBus cho khách hàng"""
    ticket_type_norm = _normalize(ticket_type)
    if "sinh viên" in ticket_type_norm or "sinh viên" in _normalize(customer_type):
        policy_key = "student_monthly"
    else:
        policy_key = "monthly"

    policy = MOCK_DATABASE["ticket_policy"].get(policy_key)
    if not policy:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy loại vé phù hợp với '{ticket_type}'"
        }, ensure_ascii=False)

    new_reg_id = f"REG{len(MOCK_DATABASE['registrations']) + 1:03d}"
    new_customer_id = f"CUS{len(MOCK_DATABASE['customers']) + 1:03d}"

    MOCK_DATABASE["customers"][new_customer_id] = {
        "customer_name": customer_name,
        "customer_type": customer_type,
        "phone_number": phone_number,
        "ticket_type": policy_key
    }

    MOCK_DATABASE["registrations"][new_reg_id] = {
        "customer_id": new_customer_id,
        "ticket_type": policy_key,
        "status": "confirmed",
        "registration_date": None
    }

    return json.dumps({
        "status": "SUCCESS",
        "registration_id": new_reg_id,
        "customer_id": new_customer_id,
        "customer_name": customer_name,
        "ticket_type": policy["name"],
        "price": policy["price"],
        "currency": policy["currency"],
        "message": f"Đăng ký vé tháng thành công cho khách hàng {customer_name}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "search_route": execute_search_route,
    "find_bus_stop": execute_find_bus_stop,
    "check_ticket_policy": execute_check_ticket_policy,
    "register_monthly_ticket": execute_register_monthly_ticket
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)


# ==============================================================================
# 3. SELF-TEST KHI CHẠY TRỰC TIẾP FILE (python src/tools.py)
# ==============================================================================

# if __name__ == "__main__":
#     print(f"✅ [TOOLS CHECK]: Đã đăng ký thành công {len(TOOLS_SCHEMA)} Native Tools trong TOOLS_SCHEMA!")

#     sample_result = dispatch_tool_call(
#         "search_route",
#         {"origin": "Mỹ Đình", "destination": "Hồ Tây"}
#     )
#     sample_data = json.loads(sample_result)
#     print(f"🧪 Kết quả gọi thử search_route: Status {sample_data['status']} (Mỹ Đình -> Hồ Tây)")
