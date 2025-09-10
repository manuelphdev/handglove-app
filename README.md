## What is Handglove App?

**Handglove App** is a comprehensive healthcare staffing and payroll management platform designed specifically for healthcare facilities to streamline their workforce operations, financial management, and administrative processes. The platform serves as a central hub for managing clinician schedules, payroll processing, vendor management, and automated financial controls.

### Primary Value Propositions

- **Automates Financial Controls**: Real-time account monitoring with SMS notifications and automated transfers
- **Streamlines Payroll Processing**: Integrated payroll with paystub generation and multiple payment methods
- **Manages Healthcare Staffing**: Shift scheduling with capacity controls and violation tracking
- **Provides Reward Systems**: Voucher programs for completed shifts and requests
- **Ensures Compliance**: Automated penalty systems and payment term enforcement
- **Scales Operations**: Multi-account system with loan management and credit controls

### Problem It Solves

Healthcare facilities traditionally struggle with complex payroll management, staff scheduling, vendor payments, and financial oversight. Handglove App automates these processes, provides real-time financial controls, and ensures proper capacity management while rewarding staff performance.


---

## Who Uses Handglove App?

### **Clinicians**

- **Daily Tasks**: Clock in/out for shifts, manage advance payments, track vouchers
- **Goals**: Complete shifts efficiently, access advance payments when needed
- **Benefits**: Automated voucher rewards, advance payment options, real-time capacity alerts

### **Supervisors**

- **Daily Tasks**: Manage requests, oversee clinician performance, track completions
- **Goals**: Ensure request completion, maintain staff productivity
- **Benefits**: Voucher rewards for completed requests, performance tracking tools

### **Schedulers**

- **Daily Tasks**: Create and manage shift posts, coordinate staffing
- **Goals**: Optimize shift coverage, ensure adequate staffing
- **Benefits**: Voucher rewards for post completions, capacity management tools

### **Facility Administrators**

- **Daily Tasks**: Monitor facility operations, review dashboards, manage finances
- **Goals**: Maintain operational efficiency, control costs, ensure compliance
- **Benefits**: Comprehensive dashboards, financial oversight, automated controls

### **COO (Chief Operating Officer)**

- **Daily Tasks**: Oversee membership management, approve credit transfers, review penalties
- **Goals**: Maintain system integrity, control financial flows, ensure compliance
- **Benefits**: Executive dashboards, credit management tools, penalty oversight

### **Vendor Partners**

- **Daily Tasks**: Process payments, manage expenses, track reimbursements
- **Goals**: Receive timely payments, manage account balances
- **Benefits**: Automated payment processing, credit management, real-time notifications

### **Accountants**

- **Daily Tasks**: Process payroll, manage accounts, generate financial reports
- **Goals**: Ensure accurate financial processing, maintain compliance
- **Benefits**: Automated payroll processing, integrated accounting, comprehensive reporting


---

## How the System is Organized

### **Multi-Account Architecture**

Each entity gets their own secure account structure with interconnected financial flows:

``` 
Handglove App Financial System
├── Working Account (Primary Operations)
│   ├── Receives invoice payments
│   ├── Funds payroll processing
│   └── Manages daily operations
├── Government Account (Tax & Compliance)
│   ├── Tax withholdings
│   ├── Penalty collections
│   └── Regulatory payments
├── Loan Account (Credit Management)
│   ├── Advance payments
│   ├── Credit transfers
│   └── Loan tracking
├── Vendor Accounts (Supplier Management)
│   ├── Vendor payments
│   ├── Expense tracking
│   └── Credit balances
└── Credit Management (Specialized Credits)
    ├── Uber Credit
    ├── Babysitter Credit
    ├── School Credit
    └── 7/11 Credit
```

### **Account Flow Benefits**

- **Real-Time Updates**: All account movements are processed immediately
- **Automated Controls**: SMS notifications and capacity checks prevent overruns
- **Audit Trail**: Complete transaction history for all account movements
- **Credit Management**: Specialized credit accounts for different expense types


---

## Core Features & Functionality

### **1. Payroll Management System**

**Purpose**: Complete payroll processing with automated calculations and paystub generation

**Key Capabilities**:

- Automated payroll calculations with overtime tracking
- PDF paystub generation with detailed breakdowns
- Multiple deduction types (Uber credit, babysitter credit, advances)
- Integration with Stripe payment processing
- Short view and full view reporting options

**Business Impact**: Eliminates manual payroll processing and ensures accurate, timely payments

### **2. Staff Scheduling & Capacity Management**

**Purpose**: Manage clinician schedules with automated capacity controls

**Key Capabilities**:

- Week view, day view, and shift view scheduling
- Automatic capacity calculation before clock-in
- Real-time hour tracking and overtime alerts
- Manual override capabilities for special circumstances
- Staff violation tracking and management

**Business Impact**: Prevents overstaffing costs and ensures adequate coverage

### **3. Invoice & Payment Gateway Integration**

**Purpose**: Process facility invoices and manage payment collections

**Key Capabilities**:

- Invoice short view and long view formats
- Integration with Invoice.com and Stripe
- Navy Federal credit union support
- Automatic account settlement after payments
- 4-hour penalty system for late payments

**Business Impact**: Accelerates payment collection and enforces payment terms

### **4. Voucher Reward System**

**Purpose**: Incentivize performance through automated voucher distribution

**Key Capabilities**:

- Eat/Gas vouchers for completed shifts (Clinicians)
- Vouchers for completed requests (Supervisors)  
- Vouchers for completed posts (Schedulers)
- Integration with Shift4.com gift card program
- Automated distribution upon task completion

**Business Impact**: Improves staff motivation and task completion rates

### **5. Advance Payment & Credit Management**

**Purpose**: Provide advance payments with automated controls and tracking

**Key Capabilities**:

- Uber and babysitter advance payments
- Monthly advance limits with automatic enforcement
- Credit deduction from future payroll
- Real-time balance tracking
- SMS notifications for credit usage

**Business Impact**: Supports staff financial needs while maintaining fiscal control

### **6. Vendor Management System**

**Purpose**: Manage vendor relationships and payment processing

**Key Capabilities**:

- Vendor account creation and management
- Expense tracking and approval workflows
- Credit balance management with SMS controls
- Real-time payment processing
- Vendor performance tracking

**Business Impact**: Streamlines vendor payments and maintains supplier relationships

### **7. Financial Dashboard & Controls**

**Purpose**: Provide real-time financial visibility and automated controls

**Key Capabilities**:

- Balance sheet dashboard with all account types
- Real-time money in/money out tracking
- Automated account transfers based on rules
- SMS notification system for critical events
- 12-month target setting and goal tracking

**Business Impact**: Enables proactive financial management and prevents cash flow issues

### **8. Membership & Subscription Management**

**Purpose**: Handle COO memberships and system access controls

**Key Capabilities**:

- COO membership management with ACH processing
- Account suspension and reactivation workflows
- Payment term modifications for penalties
- Admin search and action capabilities
- Automated billing and renewal processing

**Business Impact**: Ensures proper access control and subscription compliance


---

## User Journey & Workflows

### **Clinician Daily Workflow**

``` 
Morning:
- Check scheduled shifts
- Review capacity alerts
- Verify advance payment balance

Pre-Shift:
- System checks clinician capacity
- Clock-in enabled/disabled based on funds
- SMS notifications for any issues

During Shift:
- Automatic hour tracking
- Overtime calculations
- Real-time capacity monitoring

Post-Shift:
- Clock-out processing
- Automatic voucher distribution
- Payroll calculation updates
```

### **Supervisor Request Management**

``` 
1. Create New Request
   ↓
2. Assign to Staff Member
   ↓
3. Monitor Progress
   ↓
4. Review Completion
   ↓
5. Automatic Voucher Distribution
   ↓
6. Update Performance Metrics
```

### **Invoice Processing Workflow**

``` 
1. Invoice Generation
   ↓ (Facility services completed)
2. Client Payment Processing
   ↓ (Invoice.com/Stripe integration)
3. Account Settlement
   ↓ (Automatic posting to Working Account)
4. Government Account Update
   ↓ (Tax and penalty tracking)
5. SMS Notifications
   ↓ (Stakeholder alerts)
```

### **Payroll Processing Cycle**

``` 
Weekly Payroll:
- Collect all shift hours
- Calculate overtime and bonuses
- Deduct advances and credits
- Generate paystubs
- Process Stripe payments
- Update account balances
- Distribute vouchers earned
```


---

## System Architecture Overview

### **High-Level System Flow**

``` 
Healthcare Facilities
    ↓ (Shift Requirements)
Handglove App Platform
    ├── Scheduling System → Staff Management
    ├── Payroll Processing → Payment Systems
    ├── Financial Controls → Account Management
    ├── Vendor Management → Supplier Network
    └── Reward System → Gift Card Partners
```

### **Financial Data Flow**

``` 
Invoice Payments
    ↓
Working Account
    ├── → Payroll Processing
    ├── → Vendor Payments  
    ├── → Government Account (Taxes)
    └── → Loan Account (Advances)
         ↓
    Credit Management
    ├── Uber Credit
    ├── Babysitter Credit
    └── Other Specialized Credits
```

### **Security & Compliance**

- Real-time transaction monitoring and alerts
- Role-based access controls for all financial operations
- Complete audit logging for regulatory compliance
- Automated backup and disaster recovery
- Healthcare industry security standards compliance


---

## External Partners & Integrations

### **Payment Processing Partners**

**Stripe Integration**:
- **Purpose**: Handle payroll payments and invoice processing
- **Benefits**: Secure payment processing, automated transfers
- **User Impact**: Reliable payment delivery, reduced processing time

**Invoice.com Integration**:
- **Purpose**: Professional invoice generation and payment collection
- **Benefits**: Standardized billing format, payment tracking
- **User Impact**: Professional invoice presentation, faster collections

**Navy Federal Credit Union**:
- **Purpose**: Banking services for government and military facilities
- **Benefits**: Specialized financial services, competitive rates
- **User Impact**: Tailored banking solutions, enhanced service options

### **Gift Card & Reward Partners**

**Shift4.com Gift Card Program**:
- **Purpose**: Provide voucher rewards for staff performance
- **Benefits**: Wide merchant acceptance, automated distribution
- **User Impact**: Flexible reward redemption, immediate gratification

### **Document Processing**

**PDF Generation Systems**:
- **Purpose**: Create professional paystubs and financial documents
- **Benefits**: Standardized formatting, automated generation
- **User Impact**: Professional documentation, reduced administrative work


---

## User Roles & Access Levels

### **System Administrator (Handglove App Team)**

- **Access**: Full system access across all facilities
- **Responsibilities**: Platform management, technical support, system monitoring
- **Typical Users**: Handglove App technical staff, system administrators

### **COO (Chief Operating Officer)**

- **Access**: Executive dashboard, membership management, credit controls
- **Responsibilities**: Strategic oversight, financial controls, penalty management
- **Typical Users**: Executive leadership, financial controllers

### **Facility Administrator**

- **Access**: Full facility operations, staff management, financial dashboards
- **Responsibilities**: Daily operations, staff oversight, budget management
- **Typical Users**: Facility managers, operations directors

### **Accounting Staff**

- **Access**: Payroll processing, financial reporting, account management
- **Responsibilities**: Payroll execution, financial reconciliation, reporting
- **Typical Users**: Payroll specialists, accounting clerks, financial analysts

### **Supervisor**

- **Access**: Staff management, request processing, performance tracking
- **Responsibilities**: Staff oversight, task assignment, performance monitoring
- **Typical Users**: Shift supervisors, department heads, team leaders

### **Scheduler**

- **Access**: Shift management, capacity planning, staff assignments
- **Responsibilities**: Schedule creation, staffing optimization, coverage planning
- **Typical Users**: Scheduling coordinators, staffing managers

### **Clinician**

- **Access**: Personal schedule, time tracking, advance requests, voucher status
- **Responsibilities**: Shift completion, time reporting, advance management
- **Typical Users**: Nurses, therapists, healthcare support staff

### **Vendor Partner**

- **Access**: Payment status, account balance, expense submission
- **Responsibilities**: Service delivery, invoice submission, account maintenance
- **Typical Users**: Supply companies, service providers, contractors


---

## Key Business Processes

### **Capacity Management Process**

1. **Pre-Shift Analysis**: System calculates expected staffing costs and available funds
2. **Capacity Validation**: Compares required funds against account balances
3. **Clock-In Control**: Automatically enables/disables clock-in based on capacity
4. **Real-Time Monitoring**: Tracks hours and costs throughout shifts
5. **Automatic Cutoff**: Disables clock-out if capacity exceeded, requires manual intervention

### **Advance Payment Workflow**

1. **Request Submission**: Clinician requests advance for Uber/babysitter expenses
2. **Balance Verification**: System checks monthly advance limits and current usage
3. **Approval Process**: Automatic approval within limits, manual review for exceptions
4. **Payment Processing**: Immediate credit to appropriate account (Uber/babysitter)
5. **Payroll Deduction**: Automatic deduction from next payroll cycle

### **Voucher Distribution System**

1. **Task Completion**: System detects completed shifts, requests, or posts
2. **Eligibility Verification**: Confirms task completion meets voucher criteria
3. **Voucher Generation**: Creates gift card voucher through Shift4.com API
4. **Distribution**: Sends voucher to recipient via SMS or email
5. **Tracking**: Updates recipient's voucher history and usage records

### **Invoice Collection & Settlement**

1. **Invoice Generation**: System creates facility invoices with penalty calculations
2. **Payment Processing**: Client payments processed through Invoice.com/Stripe
3. **Account Settlement**: Payments automatically posted to Working Account
4. **Government Account Update**: Tax portions transferred to Government Account
5. **SMS Notifications**: Stakeholders notified of payment receipt and account updates

### **Penalty Application Process**

1. **Payment Due Date Monitoring**: System tracks invoice due dates
2. **Grace Period Management**: 4-hour penalty window after due date
3. **Penalty Calculation**: Automatic penalty calculation and invoice generation
4. **Account Posting**: Penalty amounts posted to Government Account
5. **Client Notification**: SMS alerts sent to clients about penalty application


---

## Implementation Considerations

### **Onboarding Requirements**

- **Financial Account Setup**: Configure all account types and banking connections
- **Staff Data Migration**: Import existing employee information and pay rates
- **Schedule Integration**: Transfer existing shift schedules and patterns
- **Vendor Setup**: Establish vendor accounts and payment terms
- **Payment Gateway Configuration**: Set up Stripe, Invoice.com, and banking integrations
- **SMS System Setup**: Configure notification preferences and contact lists

### **Success Factors**

- **Executive Sponsorship**: COO and facility leadership commitment
- **Financial Controls Training**: Staff understanding of automated controls
- **Gradual Rollout**: Phased implementation starting with core functions
- **Data Accuracy**: Clean employee and vendor data before migration
- **Process Documentation**: Clear procedures for all user roles

### **Common Challenges**

- **Complex Financial Flows**: Understanding interconnected account relationships
- **Capacity Planning**: Adjusting to automated capacity controls
- **Credit Management**: Staff adaptation to advance payment limitations
- **SMS Integration**: Ensuring reliable notification delivery
- **Multi-Role Training**: Different training needs for various user types

### **Risk Mitigation**

- **Backup Payment Methods**: Secondary payment processors for redundancy
- **Manual Override Capabilities**: Emergency procedures for system maintenance
- **Account Balance Monitoring**: Automated alerts for low balance conditions
- **Audit Trail Maintenance**: Complete transaction logging for compliance
- **Disaster Recovery**: Regular backups and recovery procedures


---

## Success Metrics & KPIs

### **Operational Metrics**

- **Schedule Compliance**: Percentage of shifts completed as scheduled
- **Capacity Accuracy**: Accuracy of pre-shift capacity calculations
- **Voucher Distribution Rate**: Percentage of earned vouchers successfully distributed
- **Advance Payment Processing Time**: Average time to process advance requests

### **Financial Metrics**

- **Payroll Accuracy**: Error rate in payroll calculations and distributions
- **Invoice Collection Rate**: Percentage of invoices paid within terms
- **Penalty Collection**: Effectiveness of 4-hour penalty enforcement
- **Account Balance Management**: Frequency of overdraft or insufficient fund situations

### **Staff Satisfaction Metrics**

- **Voucher Redemption Rate**: Percentage of distributed vouchers actually used
- **Advance Payment Utilization**: Usage rate of advance payment features
- **Clock-In Success Rate**: Percentage of attempted clock-ins that succeed
- **System Usability Score**: Staff feedback on system ease of use

### **System Performance Metrics**

- **SMS Delivery Rate**: Percentage of SMS notifications successfully delivered
- **Payment Processing Time**: Average time for payment processing and settlement
- **System Uptime**: Platform availability and reliability
- **API Response Time**: Performance of external integrations

### **Benchmark Targets**

- **98%+** Schedule compliance rate
- **95%+** Capacity calculation accuracy
- **90%+** Invoice collection within terms
- **<2 minutes** Average advance payment processing time
- **99%** SMS notification delivery rate


---

## Technical Integration Requirements

### **Payment Gateway APIs**

**Stripe Integration**:
- Real-time payment processing for payroll
- Webhook integration for payment status updates
- Automated retry logic for failed payments
- Comprehensive transaction reporting

**Invoice.com API**:
- Automated invoice generation and delivery
- Payment status tracking and updates
- Customer payment portal integration
- Remittance processing automation

### **Gift Card System Integration**

**Shift4.com Gift Card API**:
- Real-time voucher generation and distribution
- Balance checking and redemption tracking
- Merchant network integration
- Fraud prevention and security measures

### **SMS Notification System**

**Automated Alert Processing**:
- Real-time SMS delivery for critical events
- Bulk messaging for system announcements
- Delivery confirmation and retry logic
- Contact preference management

### **Banking Integration**

**Account Management APIs**:
- Real-time balance inquiries
- Automated transfer processing
- Transaction history and reporting
- Reconciliation and audit trail maintenance


---

## Glossary of Terms

### **Healthcare Staffing Terms**

- **Clinician**: Healthcare professional providing direct patient care
- **Shift**: Scheduled work period for healthcare staff
- **Capacity**: Maximum number of staff that can be scheduled based on available funds
- **Coverage**: Adequate staffing levels for facility operations
- **Overtime**: Work hours exceeding standard shift duration

### **Financial Management Terms**

- **Working Account**: Primary operating account for daily financial activities
- **Government Account**: Dedicated account for tax withholdings and regulatory payments
- **Loan Account**: Account managing advance payments and credit extensions
- **Settlement**: Process of posting payments to appropriate accounts
- **Penalty**: Financial charge applied for late payment or policy violations

### **System-Specific Terms**

- **Voucher**: Gift card reward distributed for completed tasks
- **Advance**: Pre-payment of wages for immediate expenses
- **Credit**: Pre-funded account balance for specific expense categories
- **Capacity Check**: Automated verification of available funds before scheduling
- **SMS Control**: Automated notification system for account management

### **Business Process Terms**

- **Clock-In/Clock-Out**: Time tracking system for shift management
- **Payroll Cycle**: Regular schedule for processing and distributing wages
- **Vendor Management**: System for managing supplier relationships and payments
- **Account Reconciliation**: Process of matching transactions across accounts
- **Performance Tracking**: Monitoring and measuring staff productivity and system efficiency


---
