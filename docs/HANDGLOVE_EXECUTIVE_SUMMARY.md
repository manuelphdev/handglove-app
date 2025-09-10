# Handglove Payroll System - Executive Summary

## What is Handglove?
**Handglove** is a comprehensive healthcare staffing and payroll management platform that automates workforce operations, financial controls, and administrative processes for healthcare facilities. The system provides real-time financial oversight, automated payroll processing, and staff incentive programs.

## Core Value Proposition
- **Automates Financial Controls**: Real-time account monitoring with SMS alerts and automated transfers
- **Streamlines Payroll**: Integrated payroll with paystub generation and Stripe payment processing  
- **Manages Healthcare Staffing**: Shift scheduling with capacity controls and violation tracking
- **Incentivizes Performance**: Automated voucher rewards through Shift4.com gift card program
- **Ensures Compliance**: 4-hour penalty system and automated payment term enforcement

## Key Users & Benefits

| **User Role** | **Primary Benefits** |
|---------------|---------------------|
| **Clinicians** | Automated voucher rewards, advance payments (Uber/babysitter), real-time capacity alerts |
| **Supervisors** | Performance tracking, voucher rewards for completed requests |
| **Schedulers** | Capacity management tools, voucher rewards for post completions |
| **Facility Admins** | Comprehensive dashboards, financial oversight, automated controls |
| **COO** | Executive dashboards, credit management, penalty oversight |
| **Accountants** | Automated payroll processing, integrated accounting, comprehensive reporting |

## System Architecture

### Multi-Account Financial Structure
```
Working Account (Primary) → Payroll Processing + Vendor Payments
Government Account → Tax Withholdings + Penalty Collections  
Loan Account → Advance Payments + Credit Extensions
Vendor Accounts → Supplier Management + Credit Balances
Specialized Credits → Uber, Babysitter, School, 7/11 Credits
```

### Key Integrations
- **Payment Processing**: Stripe (payroll), Invoice.com (billing), Navy Federal Credit Union
- **Reward System**: Shift4.com gift card API for automated voucher distribution
- **Notifications**: SMS system for real-time financial alerts and capacity management

## Core Features

### 1. **Automated Payroll System**
- PDF paystub generation with detailed breakdowns
- Multiple deduction types (advances, credits, overtime)
- Integration with Stripe for payment processing
- Short and full view reporting options

### 2. **Capacity Management & Scheduling**
- Pre-shift capacity calculation based on available funds
- Automatic clock-in/clock-out controls with SMS notifications
- Week/day/shift view scheduling with violation tracking
- Real-time hour tracking and overtime alerts

### 3. **Financial Dashboard & Controls**
- Real-time money in/money out tracking across all accounts
- 12-month target setting and goal tracking
- Automated account transfers based on business rules
- Balance sheet dashboard with comprehensive account visibility

### 4. **Voucher Reward System**
- Automated distribution: Eat/Gas vouchers for completed shifts (Clinicians), requests (Supervisors), and posts (Schedulers)
- Integration with Shift4.com gift card program
- Real-time distribution upon task completion

### 5. **Advance Payment & Credit Management**
- Uber and babysitter advance payments with monthly limits
- Automatic payroll deduction and real-time balance tracking
- SMS controls for credit usage and account management

## Business Process Highlights

### **Capacity Control Workflow**
1. System calculates expected staffing costs vs. available funds
2. Automatically enables/disables clock-in based on capacity
3. Real-time monitoring with automatic cutoff if exceeded
4. SMS notifications for all capacity-related events

### **Invoice & Penalty System**
1. Automated invoice generation with 4-hour penalty grace period
2. Payment processing through Invoice.com/Stripe integration
3. Automatic account settlement and government account updates
4. SMS notifications to stakeholders for payment events

### **Payroll Processing**
1. Weekly collection of shift hours and overtime calculations
2. Automatic deduction of advances and specialized credits
3. PDF paystub generation and Stripe payment processing
4. Account balance updates and earned voucher distribution

## Technical Requirements

### **Essential Integrations**
- **Stripe API**: Real-time payment processing with webhook integration
- **Invoice.com API**: Automated invoice generation and payment tracking
- **Shift4.com Gift Card API**: Voucher generation and distribution
- **SMS Gateway**: Real-time notifications and alert processing
- **Banking APIs**: Account management and automated transfers

### **Key Performance Targets**
- **98%+** Schedule compliance rate
- **95%+** Capacity calculation accuracy  
- **90%+** Invoice collection within terms
- **99%** SMS notification delivery rate
- **<2 minutes** Average advance payment processing time

## Implementation Overview

### **Phase 1: Core Financial System**
- Multi-account setup with automated transfers
- Basic payroll processing with Stripe integration
- SMS notification system implementation

### **Phase 2: Staffing & Scheduling**
- Capacity management and clock-in controls
- Shift scheduling with violation tracking
- Advance payment system for Uber/babysitter credits

### **Phase 3: Rewards & Optimization**
- Voucher system integration with Shift4.com
- Invoice processing with penalty enforcement
- Comprehensive dashboard and reporting

### **Success Metrics**
- Reduced manual payroll processing time by 80%
- Improved schedule compliance through automated capacity controls
- Enhanced staff motivation via automated reward system
- Real-time financial visibility and automated compliance enforcement

---

**Project Goal**: Create a comprehensive healthcare staffing platform that eliminates manual financial processes, ensures proper capacity management, and incentivizes staff performance through automated systems and real-time controls.
