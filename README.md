# Handglove - Healthcare Payroll & Staffing Management System

A comprehensive healthcare staffing and payroll management platform that automates workforce operations, financial controls, and administrative processes for healthcare facilities.

## 📋 Documentation

### Project Requirements
- **[Executive Summary](docs/HANDGLOVE_EXECUTIVE_SUMMARY.md)** - One-page overview of the system
- **[Complete Requirements](docs/HANDGLOVE_PAYROLL_SYSTEM_REQUIREMENTS.md)** - Detailed system specifications

### Key Features
- 🏥 **Healthcare Staffing Management** - Automated scheduling with capacity controls
- 💰 **Payroll Processing** - Integrated payroll with PDF paystubs and Stripe payments
- 🎁 **Reward System** - Automated vouchers for completed shifts and tasks
- 📱 **Real-time Notifications** - SMS alerts for financial and capacity management
- 💳 **Advance Payments** - Uber/babysitter credits with automatic payroll deduction
- 📊 **Financial Dashboard** - Multi-account tracking with automated transfers

## 🏗️ System Architecture

```
Working Account → Payroll + Vendor Payments
Government Account → Tax Withholdings + Penalties  
Loan Account → Advance Payments + Credits
Specialized Credits → Uber, Babysitter, School, 7/11
```

## 🔗 Key Integrations
- **Stripe** - Payment processing
- **Invoice.com** - Billing and invoicing
- **Shift4.com** - Gift card rewards
- **SMS Gateway** - Real-time notifications

## 👥 User Roles
- **Clinicians** - Shift management, advance payments, vouchers
- **Supervisors** - Request management, performance tracking
- **Schedulers** - Capacity planning, shift coordination
- **Admins** - Financial oversight, system management
- **COO** - Executive controls, penalty management

## 🚀 Implementation Phases

### Phase 1: Core Financial System
- Multi-account setup with automated transfers
- Basic payroll processing with Stripe integration
- SMS notification system

### Phase 2: Staffing & Scheduling  
- Capacity management and clock-in controls
- Shift scheduling with violation tracking
- Advance payment system

### Phase 3: Rewards & Optimization
- Voucher system integration
- Invoice processing with penalties
- Comprehensive reporting

## 🎯 Success Metrics
- **98%+** Schedule compliance rate
- **95%+** Capacity calculation accuracy
- **90%+** Invoice collection within terms
- **99%** SMS notification delivery rate

---

**Project Goal**: Eliminate manual financial processes, ensure proper capacity management, and incentivize staff performance through automated systems and real-time controls.

## 📄 License
This project is proprietary software developed for healthcare facility management.
