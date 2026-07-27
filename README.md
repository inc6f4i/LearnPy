# KIA PBV Life Module Easy Swap Factory

> 기아 PBV의 라이프 모듈 교체 과정을 축소 구현한  
> **Vision · Robot · PLC · Edge Computing · Agentic AI 기반 스마트팩토리 프로젝트**

<!--
프로젝트 대표 이미지 또는 시연 GIF를 아래 경로에 추가하세요.
![Project Demo](docs/images/project-demo.gif)
-->

[![Status](https://img.shields.io/badge/status-in%20progress-f59e0b)](#프로젝트-진행-현황)
[![Python](https://img.shields.io/badge/Python-Edge%20Control-3776AB?logo=python&logoColor=white)](#기술-스택)
[![Vision](https://img.shields.io/badge/Vision-YOLOv8%20%2B%20OpenCV-5C3EE8)](#vision-시스템)
[![Database](https://img.shields.io/badge/MariaDB-Planned-9ca3af?logo=mariadb&logoColor=white)](#database-planned)

---

## 목차

- [프로젝트 개요](#프로젝트-개요)
- [프로젝트 목표](#프로젝트-목표)
- [왜 PBV인가](#왜-pbv인가)
- [시스템 아키텍처](#시스템-아키텍처)
  - [전체 토폴로지](#전체-토폴로지)
  - [Physical Factory](#physical-factory)
  - [Edge Computing](#edge-computing)
  - [AI Inference Server — Optional](#ai-inference-server--optional)
- [Dual-Track 생산 공정](#dual-track-생산-공정)
- [기술 스택](#기술-스택)
- [Vision 시스템](#vision-시스템)
- [Vision + Multi Object Tracking](#vision--multi-object-tracking)
- [Agentic AI](#agentic-ai)
- [수요 예측과 모듈 사전 준비](#수요-예측과-모듈-사전-준비)
- [Vision-AI-PLC 연계](#vision-ai-plc-연계)
- [Database — Planned](#database-planned)
- [안전 및 제어 원칙](#안전-및-제어-원칙)
- [프로젝트 진행 현황](#프로젝트-진행-현황)
- [성능 평가 계획](#성능-평가-계획)
- [로드맵](#로드맵)
- [예정 디렉터리 구조](#예정-디렉터리-구조)

---

## 프로젝트 개요

**KIA PBV Life Module Easy Swap Factory**는 고객의 예약과 목적에 맞춰 PBV의 라이프 모듈을 자동으로 교체하는 공정을 스마트팩토리 형태로 구현하는 프로젝트입니다.

차량에서 **기존 모듈을 분리·회수하는 흐름**과 창고에서 **새 모듈을 준비·공급하는 흐름**을 동시에 관리하고, 두 흐름이 Easy Swap Station에서 합류하도록 설계합니다. 공정에는 DOBOT 로봇, Mitsubishi PLC, CIMON SCADA, 카메라 기반 Vision, Edge Computer 및 Agentic AI가 연동됩니다.

Vision은 단순한 최종 검사 장치가 아닙니다. 각 모듈에 추적 ID를 부여해 이동과 공정 상태를 계속 추적하고, 로봇 작업을 위한 위치 정보와 조립 검사 결과를 제공합니다. AI Agent는 축적된 생산·고객 데이터를 분석해 향후 수요를 예측하고 필요한 모듈을 미리 준비하도록 생산계획을 지원합니다.

> 본 프로젝트는 교육 및 PoC(Proof of Concept)를 위한 축소형 스마트팩토리 구현을 목표로 합니다.

---

## 프로젝트 목표

- PBV 라이프 모듈의 분리, 공급, 장착 및 검사를 하나의 자동화 공정으로 통합
- 제거 모듈과 신규 모듈을 동시에 관리하는 Dual-Track 물류 흐름 구현
- Python과 PyDobot을 이용한 DOBOT 제어 및 엣지 기반 통합 제어
- Mitsubishi PLC를 통한 센서, 액추에이터, 인터록 및 안전 시퀀스 제어
- CIMON SCADA 기반 설비 상태 및 공정 진행 상황 모니터링
- YOLOv8, OpenCV 및 Multi Object Tracking을 이용한 모듈 검출·추적·검사
- Vision, Robot, PLC 사이의 작업 상태와 핸드셰이크 표준화
- 생산 및 고객 데이터 기반 모듈 수요 예측과 사전 준비
- 향후 MariaDB, Digital Twin, MQTT 및 다중 로봇 환경으로 확장 가능한 구조 확보

---

## 왜 PBV인가

기존 차량은 생산 이후 용도와 실내 구성이 대부분 고정됩니다. 반면 PBV는 목적에 맞는 공간과 서비스를 제공할 수 있도록 설계되며, 라이프 모듈 개념을 적용하면 하나의 차량 플랫폼을 다양한 용도로 전환할 수 있습니다.

| 활용 목적 | 라이프 모듈 예시 |
|---|---|
| 여객 | 셔틀, 이동 편의 공간 |
| 물류 | 소형 배송, 적재 최적화 |
| 레저 | 캠핑, 아웃도어 |
| 의료 | 이동 진료, 응급 지원 |
| 업무 | 이동형 오피스, 서비스 공간 |

이 프로젝트가 다루는 핵심은 차량 자체보다 **모듈 교체를 안정적이고 반복 가능하게 운영하는 공장 시스템**입니다. 고객 주문과 수요 변화에 따라 필요한 모듈을 준비하고, 분리된 모듈은 검사 후 회수하며, 신규 모듈은 적시에 공급해 차량 대기시간을 줄입니다.

---

## 시스템 아키텍처

### 전체 토폴로지

```text
 Customer / Operator
         │
         │ Reservation · Module Request
         ▼
┌───────────────────────┐
│ MES / Service Server  │
│ Work Order · Schedule │
└───────────┬───────────┘
            │
            ├──────────────────────────────────────┐
            │                                      │
            ▼                                      ▼
┌───────────────────────┐              ┌────────────────────────┐
│     CIMON SCADA       │              │ AI Inference Server    │
│ Monitor · HMI · Alarm │              │ (Optional / Separable) │
└───────────┬───────────┘              │ Forecast · Agent · LLM │
            │                          └────────────┬───────────┘
            │ Ethernet / PLC Protocol              │ REST / MQTT
            ▼                                      │
┌───────────────────────┐              ┌────────────▼───────────┐
│    Mitsubishi PLC     │◄────────────►│     Edge Computer      │
│ Sequence · I/O        │ Handshake    │ Python Orchestration   │
│ Interlock · Safety    │              │ Vision · PyDobot       │
└──────┬─────────┬──────┘              └──────┬─────────┬───────┘
       │         │                            │         │
       │         │                            │         │
       ▼         ▼                            ▼         ▼
  Conveyor   Sensors /                Vision Camera   DOBOT
             Actuators                 Detection &    Robot
                                       Tracking
            │                                      │
            └──────────── Physical Factory ────────┘

                      ┌────────────────────────┐
                      │ MariaDB (Planned)      │
                      │ History · Quality · AI │
                      └────────────────────────┘
```

이 구조는 제어 책임을 세 계층으로 분리합니다.

1. **현장 제어 계층** — PLC가 설비 I/O, 인터록 및 결정적 시퀀스를 담당합니다.
2. **엣지 계층** — Python 애플리케이션이 Vision, 추적, PyDobot 및 작업 오케스트레이션을 통합합니다.
3. **지능화 계층** — AI 서버가 분석, 예측 및 생산계획 권고를 담당하며 필요하면 별도 GPU 서버로 분리합니다.

<!--
고해상도 아키텍처 이미지를 추가할 경우:
![System Architecture](docs/images/system-architecture.png)
-->

### Physical Factory

```text
                           EASY SWAP CELL

 Removed Module Track                         New Module Track
┌──────────────────────┐                    ┌──────────────────────┐
│ Vehicle Arrival      │                    │ Module Storage       │
│ Vehicle ID Check     │                    │ Order-based Release  │
└──────────┬───────────┘                    └──────────┬───────────┘
           │                                           │
           ▼                                           ▼
┌──────────────────────┐                    ┌──────────────────────┐
│ Module Detachment    │                    │ Incoming Vision      │
│ Robot + Interlock    │                    │ Type · Pose · Quality│
└──────────┬───────────┘                    └──────────┬───────────┘
           │                                           │
           ▼                                           ▼
┌──────────────────────┐                    ┌──────────────────────┐
│ Removed Module       │                    │ Conveyor Supply      │
│ Tracking / Inspection│                    │ Tracking by ID       │
└──────────┬───────────┘                    └──────────┬───────────┘
           │                                           │
           └──────────────────┬────────────────────────┘
                              ▼
                   ┌──────────────────────┐
                   │ Easy Swap Station    │
                   │ Position · Assemble  │
                   └──────────┬───────────┘
                              ▼
                   ┌──────────────────────┐
                   │ Final Vision Check   │
                   │ Presence · Pose · ID │
                   └──────────┬───────────┘
                              ▼
                   ┌──────────────────────┐
                   │ Complete / Release   │
                   │ History (Planned)    │
                   └──────────────────────┘
```

주요 물리 장치는 다음과 같습니다.

- DOBOT 로봇 및 로봇 컨트롤러
- 차량·모듈 이송용 컨베이어
- 모듈 감지, 위치 확인 및 안전 확인 센서
- 검출·추적·검사용 카메라
- Mitsubishi PLC 및 현장 I/O
- Edge Computer
- 운영자용 CIMON SCADA/HMI

### Edge Computing

Edge Computer는 현장과 가까운 위치에서 저지연 처리가 필요한 Python 기반 기능을 통합합니다.

```text
┌─────────────────────────────────────────────────────┐
│                  EDGE COMPUTER                      │
├─────────────────────────────────────────────────────┤
│ Work Orchestrator                                   │
│  ├─ Work-order state machine                        │
│  ├─ Dual-track synchronization                      │
│  └─ Error / retry policy                            │
│                                                     │
│ Robot Control                                       │
│  ├─ Python                                          │
│  ├─ PyDobot                                         │
│  └─ Motion request / result                         │
│                                                     │
│ Vision & Tracking                                   │
│  ├─ YOLOv8 detection                                │
│  ├─ OpenCV preprocessing / calibration              │
│  ├─ Multi Object Tracking                           │
│  └─ Inspection / position correction                │
│                                                     │
│ Factory Interfaces                                  │
│  ├─ PLC handshake                                   │
│  ├─ SCADA status                                    │
│  ├─ AI API client (Optional)                        │
│  └─ MariaDB client (Planned)                        │
└─────────────────────────────────────────────────────┘
```

PLC와 Edge Computer는 경쟁적으로 같은 장치를 제어하지 않습니다. PLC는 설비 상태와 실행 가능 여부를 판단하고, Edge Computer는 승인된 상태에서 로봇 작업 요청과 Vision 처리를 조율합니다.

### AI Inference Server — Optional

초기 PoC에서는 Edge Computer 안에서 일부 AI 기능을 실행할 수 있습니다. 모델 규모, GPU 요구량 또는 여러 생산 셀의 동시 사용량이 증가하면 AI 기능을 별도 서버로 분리합니다.

```text
┌───────────────────────┐   REST API / MQTT   ┌────────────────────────┐
│     Edge Computer     │◄───────────────────►│  AI Inference Server   │
│ Real-time Factory App │                     │                        │
│ Local Vision / Cache  │                     │ Demand Forecasting     │
└───────────┬───────────┘                     │ Agentic AI             │
            │                                 │ Report Generation      │
            ▼                                 │ Model Serving / GPU    │
┌───────────────────────┐                     └────────────────────────┘
│ Mitsubishi PLC       │
│ Validated Commands   │
└───────────────────────┘
```

네트워크 또는 AI 서버에 장애가 발생해도 PLC의 안전 로직과 기본 공정 제어는 유지되어야 합니다. AI의 출력은 **권고 또는 검증 대상 명령**으로 취급하며, 현장 실행 전 상태·권한·인터록을 확인합니다.

---

## Dual-Track 생산 공정

하나의 모듈이 하나의 고정 작업만 수행하는 방식이 아니라, 각 모듈의 추적 ID와 현재 상태에 따라 필요한 작업이 결정됩니다. 제거 모듈과 신규 모듈은 서로 다른 경로로 움직이지만 Easy Swap Station의 작업 조건에 맞춰 동기화됩니다.

```text
                    Vehicle Arrival / Work Order
                               │
                      Vehicle & Order Match
                               │
            ┌──────────────────┴──────────────────┐
            │                                     │
            ▼                                     ▼
   TRACK A — REMOVED MODULE              TRACK B — NEW MODULE
   1. Existing module identify           1. Required module select
   2. Unlock / detach                    2. Storage release
   3. Robot unload                       3. Type / pose inspection
   4. Tracking ID maintain               4. Conveyor tracking
   5. Condition inspection               5. Arrival-time control
   6. Return / repair / storage          6. Swap-station standby
            │                                     │
            └──────────────────┬──────────────────┘
                               ▼
                     Easy Swap Synchronization
                               │
                       Robot Positioning
                               │
                       Module Installation
                               │
                   Final Vision / ID Verification
                               │
              ┌────────────────┴────────────────┐
              │                                 │
             PASS                         RETRY / HOLD
              │                                 │
      History & Vehicle Release       Reinspect / Operator Review
```

### Track A — 교체된 모듈

- 차량 및 장착 모듈 식별
- 잠금 해제 조건과 안전 상태 확인
- 로봇을 이용한 분리 및 하역
- 분리 후에도 동일한 추적 ID 유지
- 외관, 방향, 상태 및 재사용 가능 여부 검사
- 검사 결과에 따라 보관, 정비, 재검 또는 폐기 대기 경로로 분기

### Track B — 교체할 모듈

- 고객 주문과 작업지시에 맞는 모듈 선택
- 창고 또는 버퍼에서 모듈 출고
- Vision으로 종류, 방향, 위치 및 기본 품질 확인
- 컨베이어 이동 중 지속 추적
- Easy Swap Station 도착 시점 조절
- 차량·작업지시·모듈 ID가 모두 일치할 때 장착 허용

### 두 트랙의 동기화 조건

```text
Removed_Module_Clear
AND New_Module_Ready
AND Vehicle_Position_OK
AND Robot_Ready
AND Safety_Interlock_OK
AND Work_Order_Matched
────────────────────────────────
= Assembly_Enable
```

---

## 기술 스택

| 영역 | 기술 / 장비 | 제어·연동 방식 | 주요 역할 | 상태 |
|---|---|---|---|---|
| Robot | DOBOT | Python + PyDobot | 모듈 분리, 이송, 장착 | In Progress |
| Edge Control | Edge Computer | Python Runtime | 공정 오케스트레이션, Vision·Robot·PLC 연계 | In Progress |
| PLC | Mitsubishi PLC | PLC Logic + Ethernet 기반 통신 | I/O, 시퀀스, 인터록, 안전 조건 | In Progress |
| SCADA | CIMON SCADA | PLC 모니터링 및 HMI | 상태 표시, 알람, 운영자 명령 | Planned |
| Detection | YOLOv8 | Python Inference | 모듈·부품 검출 및 분류 | In Progress |
| Image Processing | OpenCV | Python | 전처리, 보정, 좌표 변환, 검사 | In Progress |
| Tracking | Multi Object Tracking | Python | 이동 객체 ID 및 공정 이력 연속성 유지 | In Progress |
| AI Agent | Agentic AI + Python | REST API 또는 로컬 호출 | 분석, 예측, 계획 권고, 보고 | Planned |
| Database | MariaDB | Python DB Client / ORM | 생산·검사·이벤트 이력 저장 | Planned |
| Messaging | MQTT | Publish / Subscribe | 설비·서버 간 이벤트 연동 | Roadmap |
| Visualization | Dashboard / Digital Twin | API / MQTT | 생산 현황 및 가상 공정 표현 | Roadmap |

> 실제 PLC 통신 프로토콜과 주소 체계는 사용 PLC 모델, 통신 모듈 및 현장 구성 확정 후 문서화합니다.

---

## Vision 시스템

Vision은 입고 검사, 이동 추적, 로봇 위치 보정, 장착 확인 및 최종 검사까지 공정 전반에 사용됩니다.

### Vision Pipeline

```text
Camera Frame
     │
     ▼
OpenCV Preprocessing
Resize · Undistort · ROI · Color Conversion
     │
     ▼
YOLOv8 Detection
Class · Confidence · Bounding Box
     │
     ▼
Multi Object Tracking
Track ID · Position · Direction · Timestamp
     │
     ├─────────────────────┐
     ▼                     ▼
Robot Position Data    Process Inspection
Coordinate Transform   Type · Pose · Presence
     │                     │
     └──────────┬──────────┘
                ▼
        Decision / Result Packet
                │
                ▼
       Edge State Machine → PLC Handshake
```

### 검사 및 인식 대상

- 라이프 모듈 종류와 모듈 ID
- 모듈의 위치, 방향 및 회전 상태
- 컨베이어 내 이동 방향과 구역 점유 여부
- 로봇 Pick & Place를 위한 좌표 보정값
- 장착 전후 모듈 존재 여부
- 조립 완료 여부와 오장착 여부
- 향후 확장: Scratch, Gap, 체결 상태 및 표면 결함

### 좌표 처리 개념

```text
Pixel Coordinate
      │ Camera Calibration
      ▼
Camera Coordinate
      │ Hand-Eye / Workspace Transform
      ▼
Robot Coordinate
      │ Range & Safety Validation
      ▼
Approved Motion Request
```

Vision이 계산한 좌표를 곧바로 로봇에 전달하지 않습니다. 작업 영역, 신뢰도, 추적 상태 및 PLC 인터록을 확인한 뒤 유효한 요청만 실행합니다.

<!--
추론 결과 이미지 예시:
![YOLO Detection Result](docs/images/vision-detection-result.jpg)

추적 시연 GIF:
![Multi Object Tracking](docs/images/multi-object-tracking.gif)
-->

---

## Vision + Multi Object Tracking

검출은 한 프레임 안에서 객체를 찾지만, 추적은 여러 프레임과 공정 구간에 걸쳐 **같은 모듈의 연속성**을 유지합니다.

```text
Frame t                 Frame t+1               Process Event
┌─────────────┐         ┌─────────────┐         ┌─────────────────┐
│ Module A    │ Match   │ Module A    │ Update  │ Track ID: 1042  │
│ bbox + cls  ├────────►│ bbox + cls  ├────────►│ Zone: INBOUND   │
└─────────────┘         └─────────────┘         │ State: INSPECTED│
                                               └─────────────────┘
```

하나의 모듈은 공정 상황에 따라 복수의 작업을 거칠 수 있습니다.

```text
DETECTED
   │
   ▼
IDENTIFIED
   │
   ├── Removed Module → DETACHED → INSPECTED → RETURN / REPAIR / STORE
   │
   └── New Module     → RELEASED → TRACKED → INSTALLED → VERIFIED
```

추적 시스템이 유지해야 할 주요 정보는 다음과 같습니다.

| 필드 | 설명 |
|---|---|
| `track_id` | Vision 추적 세션 내 객체 식별자 |
| `module_id` | 실제 라이프 모듈 식별자 |
| `module_type` | 캠핑, 물류, 승객 등 모듈 종류 |
| `work_order_id` | 연결된 작업지시 |
| `current_zone` | 창고, 컨베이어, 교체 셀 등 현재 구역 |
| `process_state` | 검출, 검사, 대기, 장착 등 상태 |
| `confidence` | 검출 또는 판정 신뢰도 |
| `last_seen_at` | 마지막 관측 시각 |

---

## Agentic AI

Agentic AI는 로봇을 직접 움직이는 실시간 제어기가 아니라, 생산 데이터를 해석하고 다음 행동을 제안하는 **상위 의사결정 지원 계층**입니다.

### 역할 계층

```text
LEVEL 3 — DEMAND & PRODUCTION PLANNING
Seasonality · Customer Needs · Module Preference · Inventory
                         │
                         ▼
LEVEL 2 — ANALYSIS & OPTIMIZATION
Cycle Time · Defect Trend · Bottleneck · Preparation Priority
                         │
                         ▼
LEVEL 1 — OPERATIONAL ASSISTANCE
Vision Result Summary · Reinspection Proposal · Operator Report
                         │
                         ▼
VALIDATION LAYER
Rule Check · Permission · PLC State · Safety Interlock
                         │
                         ▼
PLC / EDGE EXECUTION
```

### 주요 기능

- Vision 결과와 공정 이벤트 요약
- 오류 유형 분류 및 재검사·보류·운영자 확인 제안
- 작업 완료 보고서와 교대 보고서 생성
- Cycle Time, 불량률 및 병목 구간 분석
- 기간, 지역, 고객 선호 및 예약 데이터를 이용한 모듈 수요 예측
- 예상 수요에 따른 모듈 준비 우선순위와 재고 배치 권고
- 데이터가 부족하거나 위험도가 높은 경우 운영자 승인 요청

### Agent 처리 흐름

```text
Observe
PLC State + Vision Result + Work Order + Inventory
   │
   ▼
Analyze
Context Check + Forecast + Anomaly Classification
   │
   ▼
Plan
Recommended Action + Reason + Confidence
   │
   ▼
Validate
Business Rule + Permission + Safety Boundary
   │
   ├── Invalid / Unsafe → Reject + Alert
   │
   ├── Uncertain        → Operator Approval
   │
   └── Valid            → Edge/PLC Request
   ▼
Record
Input + Decision + Result + Feedback (Database Planned)
```

---

## 수요 예측과 모듈 사전 준비

Agent는 축적된 생산·예약·고객 데이터를 이용해 어떤 라이프 모듈의 수요가 증가할지 예측합니다. 예를 들어 휴가철에는 캠핑 모듈, 특정 시간대나 지역에서는 물류 또는 승객 모듈의 선호도가 높아질 수 있습니다.

```text
Historical Swap Data ───────┐
Reservation / Order Data ───┤
Season / Holiday / Weekday ─┤
Region / Service Area ──────┼──► Feature Pipeline
Customer Preference ────────┤           │
Inventory / Lead Time ──────┘           ▼
                                  Demand Forecast
                                        │
                         ┌──────────────┼──────────────┐
                         ▼              ▼              ▼
                   Module Type     Time Window     Confidence
                         │              │              │
                         └──────────────┼──────────────┘
                                        ▼
                              Preparation Recommendation
                                        │
                         ┌──────────────┼──────────────┐
                         ▼              ▼              ▼
                    Pre-position     Inspection     Inventory
                    Module           Priority       Replenishment
                                        │
                                        ▼
                              Reduced Waiting Time
```

### 예측 출력 예시

```json
{
  "forecast_window": "2026-08-01T09:00:00+09:00/2026-08-01T18:00:00+09:00",
  "module_type": "CAMPING",
  "expected_demand": 12,
  "recommended_ready_quantity": 14,
  "confidence": 0.84,
  "factors": ["summer_holiday", "weekend", "recent_reservations"]
}
```

예측 결과는 생산계획 또는 운영자에게 제안되며, 실제 모듈 출고 명령은 재고·작업지시·설비 상태를 확인한 후 실행합니다.

---

## Vision-AI-PLC 연계

세 시스템은 목적과 시간 특성이 다릅니다.

| 시스템 | 시간 특성 | 책임 |
|---|---|---|
| Vision / Edge | 저지연 | 검출, 추적, 좌표 및 검사 결과 생성 |
| AI Agent | 비실시간·준실시간 | 분석, 예측, 설명 및 작업 권고 |
| PLC | 결정적·실시간 | 인터록, I/O, 시퀀스 및 실행 승인 |

```text
                 ┌────────────────────┐
                 │ Vision Camera      │
                 └─────────┬──────────┘
                           ▼
                 ┌────────────────────┐
                 │ Edge Vision        │
                 │ Detect + Track     │
                 └──────┬───────┬─────┘
                        │       │
        Inspection Data │       │ Position / State
                        ▼       ▼
              ┌────────────┐  ┌────────────────┐
              │ AI Agent   │  │ Edge Control   │
              │ Analyze /  │  │ State Machine  │
              │ Recommend  │  │ PyDobot        │
              └─────┬──────┘  └───────┬────────┘
                    │ Validated Request │ Handshake
                    └──────────┬────────┘
                               ▼
                    ┌────────────────────┐
                    │ Mitsubishi PLC     │
                    │ Interlock / I/O    │
                    └───────┬────────────┘
                            │ Execute Permit
                            ▼
                   Robot / Conveyor / I/O
```

### 권장 핸드셰이크

```text
Edge/Robot Side                         PLC Side
---------------                         --------
JOB_REQUEST        ───────────────────► Validate state
                    ◄────────────────── ROBOT_ENABLE
ROBOT_BUSY         ───────────────────► Hold conflicting motion
ROBOT_DONE         ───────────────────► Verify sensor state
                    ◄────────────────── JOB_ACK

On fault:
ROBOT_ERROR + CODE ───────────────────► Stop sequence / alarm
                    ◄────────────────── RESET_PERMISSION
```

### 검사 결과 상태

| 상태 | 의미 | 기본 처리 |
|---|---|---|
| `PASS` | 기준 충족 | 다음 공정 요청 |
| `RETRY` | 이미지 또는 판정 불확실 | 재촬영·재검사 |
| `HOLD` | 오장착, ID 불일치 등 | 공정 보류 및 운영자 확인 |
| `FAULT` | 설비·통신·안전 이상 | PLC 시퀀스 정지 및 알람 |

---

## Database — Planned

MariaDB는 향후 생산 이력, Vision 결과, 설비 이벤트 및 AI 학습·평가 데이터를 통합 저장하기 위한 기능으로 계획되어 있습니다. 현재 단계에서는 스키마와 데이터 계약을 우선 설계합니다.

### 예정 데이터 영역

| 영역 | 주요 데이터 |
|---|---|
| Vehicle | 차량 ID, 입고·출고 시각, 현재 상태 |
| Work Order | 작업지시 ID, 요청 모듈, 우선순위, 진행 상태 |
| Module | 모듈 ID, 종류, 위치, 상태, 누적 사용 횟수 |
| Tracking | Track ID, 구역, 좌표, 관측 시각 |
| Vision Result | 이미지 참조, 클래스, 신뢰도, 판정, 결함 유형 |
| Robot Cycle | 작업 종류, 시작·종료, Cycle Time, 결과 |
| Equipment Event | 설비 ID, 이벤트 코드, 심각도, 발생 시각 |
| Agent Decision | 입력 요약, 권고, 근거, 신뢰도, 승인 결과 |
| Demand Forecast | 예측 기간, 모듈 종류, 수요량, 실제 결과 |

### 개념적 관계

```text
Vehicle 1 ─── N WorkOrder N ─── 1 Module
                    │
                    ├── N VisionResult
                    ├── N RobotCycle
                    ├── N EquipmentEvent
                    └── N AgentDecision

Module 1 ─── N TrackingEvent
Module 1 ─── N DemandForecastResult
```

데이터베이스 도입 전에도 이벤트 이름, 타임스탬프, ID 규칙 및 상태 코드를 통일해 향후 마이그레이션 비용을 줄입니다.

---

## 안전 및 제어 원칙

- PLC가 현장 인터록과 안전 관련 실행 조건의 최종 책임을 가집니다.
- AI Agent는 비상정지 장치나 안전 PLC를 대체하지 않습니다.
- Edge Computer 또는 AI 서버 장애 시 안전 상태로 전환할 수 있어야 합니다.
- Vision 좌표는 작업 범위, 신뢰도 및 캘리브레이션 상태를 검증한 후 사용합니다.
- 차량, 작업지시 및 모듈 ID가 일치하지 않으면 장착을 허용하지 않습니다.
- 재시도 횟수와 타임아웃을 제한하고, 반복 실패는 운영자 확인으로 전환합니다.
- 모든 수동·자동 명령은 실행 주체와 결과를 추적할 수 있도록 기록합니다.

> 실제 장비 적용 시에는 장비 제조사 매뉴얼, 위험성 평가 및 현장 안전 규정을 기준으로 별도의 안전 설계를 수행해야 합니다.

---

## 프로젝트 진행 현황

| 항목 | 상태 | 산출물 / 목표 |
|---|---|---|
| 프로젝트 주제 및 범위 선정 | ✅ Completed | PBV Easy Swap PoC 정의 |
| PBV 및 라이프 모듈 조사 | ✅ Completed | 적용 개념 정리 |
| 기본 시스템 아키텍처 | ✅ Completed | Physical / Edge / AI 계층 설계 |
| Dual-Track 공정 설계 | ✅ Completed | 제거·신규 모듈 흐름 정의 |
| 3D 모델링 및 셀 배치 | 🔄 In Progress | 장비 배치와 작업영역 검토 |
| DOBOT + PyDobot 제어 | 🔄 In Progress | 기본 Motion 및 작업 시퀀스 |
| YOLOv8 객체 검출 | 🔄 In Progress | 데이터셋 및 검출 모델 구축 |
| Multi Object Tracking | 🔄 In Progress | 모듈 ID 연속성 유지 |
| PLC 시퀀스 및 인터록 | 🔄 In Progress | I/O와 핸드셰이크 구현 |
| CIMON SCADA | 📅 Planned | 화면, 알람, 상태 모니터링 |
| Agentic AI | 📅 Planned | 분석·권고·보고 워크플로 |
| MariaDB | 📅 Planned | 생산·품질·예측 데이터 저장 |
| 실장비 통합 시험 | 📅 Planned | End-to-End 시나리오 검증 |

> 상태 표는 구현 진행에 맞춰 지속적으로 갱신합니다.

---

## 성능 평가 계획

구현 결과는 다음 지표로 검증할 예정입니다.

| 분류 | 지표 | 측정 목적 |
|---|---|---|
| Vision | Precision, Recall, mAP | 모듈 검출 성능 |
| Tracking | ID Switch, Track Loss | 추적 연속성 |
| Inspection | PASS/FAIL Accuracy | 검사 판정 신뢰성 |
| Robot | Pick/Place Success Rate | 작업 반복성 |
| Process | Swap Cycle Time | 전체 교체 시간 |
| Synchronization | Track Waiting Time | Dual-Track 균형 |
| Reliability | Error / Recovery Rate | 장애 대응 능력 |
| Forecast | MAE, MAPE 또는 WAPE | 수요 예측 오차 |
| Business | Module Ready Rate | 사전 준비 효과 |

<!--
성능 결과가 확보되면 아래 이미지를 추가하세요.
![Performance Dashboard](docs/images/performance-dashboard.png)
-->

---

## 로드맵

### Phase 1 — Factory Cell Foundation

- [x] 프로젝트 범위와 공정 개념 정의
- [x] 시스템 계층 및 Dual-Track 구조 설계
- [ ] 3D 셀 구성과 좌표계 확정
- [ ] DOBOT 기본 동작 및 PyDobot 제어
- [ ] PLC I/O 맵과 인터록 정의

### Phase 2 — Vision & Tracking

- [ ] 데이터 수집 및 라벨링
- [ ] YOLOv8 모듈 검출
- [ ] OpenCV 캘리브레이션과 좌표 변환
- [ ] Multi Object Tracking
- [ ] 로봇 위치 보정 및 장착 검사

### Phase 3 — Integrated Control

- [ ] Edge 상태 머신
- [ ] PLC-Edge-Robot 핸드셰이크
- [ ] CIMON SCADA 화면 및 알람
- [ ] Dual-Track 동기화
- [ ] End-to-End 자동 교체 시나리오

### Phase 4 — Data & Agentic AI

- [ ] MariaDB 스키마 및 이벤트 저장
- [ ] 생산·검사 Dashboard
- [ ] Agent 작업 보고 및 이상 분류
- [ ] 수요 예측 모델
- [ ] 모듈 사전 준비 권고

### Phase 5 — Scale-up

- [ ] MQTT 이벤트 기반 연동
- [ ] Digital Twin
- [ ] Predictive Maintenance
- [ ] AGV 및 자동 창고 연동
- [ ] Multi-Robot Scheduler
- [ ] 별도 GPU AI Inference Server

---

## 예정 디렉터리 구조

```text
kia-pbv-easy-swap-factory/
├─ README.md
├─ docs/
│  ├─ architecture/
│  ├─ images/
│  ├─ plc-io-map/
│  └─ test-results/
├─ edge/
│  ├─ app/
│  ├─ config/
│  ├─ interfaces/
│  │  ├─ plc/
│  │  ├─ robot/
│  │  └─ vision/
│  └─ tests/
├─ robot/
│  ├─ pydobot_controller/
│  ├─ motion/
│  └─ calibration/
├─ vision/
│  ├─ datasets/
│  ├─ detection/
│  ├─ tracking/
│  ├─ inspection/
│  └─ calibration/
├─ plc/
│  ├─ sequence/
│  ├─ io-map/
│  └─ handshake/
├─ scada/
│  ├─ screens/
│  └─ alarms/
├─ agent/
│  ├─ workflows/
│  ├─ forecasting/
│  ├─ prompts/
│  └─ evaluation/
├─ database/
│  ├─ schema/
│  └─ migrations/
└─ scripts/
```

> 위 구조는 목표 아키텍처를 나타냅니다. 실제 구현 범위와 저장소 구성에 맞춰 조정할 예정입니다.

---

## 프로젝트 핵심 요약

```text
Dual-Track Material Flow
        +
Vision Detection & Tracking
        +
Python / PyDobot Edge Control
        +
PLC Interlock & SCADA Monitoring
        +
Agentic AI Demand Forecasting
        =
PBV Life Module Easy Swap Smart Factory
```

이 프로젝트는 단순한 로봇 Pick & Place 데모를 넘어, **모듈의 전 공정 추적**, **두 물류 흐름의 동기화**, **안전한 계층형 제어**, **축적 데이터 기반 수요 예측**을 하나의 스마트팩토리 구조로 통합하는 것을 목표로 합니다.

---

## License

라이선스는 프로젝트 공개 범위와 사용 장비·데이터의 권리를 검토한 후 결정할 예정입니다.

