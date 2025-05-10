
# **Purple Vibes Backend API**

## 🧪 Testing

### 📚 Table of Contents

* [Code Validation](#code-validation)
* [Automated Testing](#automated-testing)
* [Manual Testing](#manual-testing)
* [Known Issues](#known-issues)

---

## ✅ Code Validation

Code validation was performed using **PEP8** standards. The `pycodestyle` linter was configured in GitPod using the following steps:

1. Install pycodestyle:

   ```bash
   pip3 install pycodestyle
   ```
2. Open the Command Palette (`Ctrl+Shift+P`).
3. Search for `Python: Select Linter` and choose `pycodestyle`.
4. Navigate to `View` → `Problems` to see linting results.

All Python files across the project passed without warnings or errors.

### Breakdown by App:

<details>
<summary><strong>Events API</strong></summary>

* ✅ `permissions.py`
* ✅ `serializers.py`
* ✅ `views.py`
* ✅ `models.py`
* ✅ `urls.py`

</details>

<details>
<summary><strong>Comments</strong></summary>

* ✅ `models.py`
* ✅ `serializers.py`
* ✅ `tests.py`
* ✅ `urls.py`
* ✅ `views.py`

</details>

<details>
<summary><strong>Contact</strong></summary>

* ✅ `models.py`
* ✅ `serializers.py`
* ✅ `tests.py`
* ✅ `urls.py`
* ✅ `views.py`

</details>

<details>
<summary><strong>Events</strong></summary>

* ✅ `models.py`
* ✅ `serializers.py`
* ✅ `tests.py`
* ✅ `urls.py`
* ✅ `views.py`

</details>

<details>
<summary><strong>Followers</strong></summary>

* ✅ `models.py`
* ✅ `serializers.py`
* ✅ `tests.py`
* ✅ `urls.py`
* ✅ `views.py`

</details>

<details>
<summary><strong>Going</strong></summary>

* ✅ `models.py`
* ✅ `serializers.py`
* ✅ `tests.py`
* ✅ `urls.py`
* ✅ `views.py`

</details>

<details>
<summary><strong>Interested</strong></summary>

* ✅ `models.py`
* ✅ `serializers.py`
* ✅ `tests.py`
* ✅ `urls.py`
* ✅ `views.py`

</details>

<details>
<summary><strong>Profiles</strong></summary>

* ✅ `models.py`
* ✅ `serializers.py`
* ✅ `tests.py`
* ✅ `urls.py`
* ✅ `views.py`

</details>

<details>
<summary><strong>Reviews</strong></summary>

* ✅ `models.py`
* ✅ `serializers.py`
* ✅ `tests.py`
* ✅ `urls.py`
* ✅ `views.py`

</details>

---

## 🤖 Automated Testing

Each app includes unit and integration tests written using Django’s built-in test framework. Below is a summary of tested functionalities:

![Automated Test Summary](images/test-summary.png)

<details>
<summary><strong>Profiles</strong></summary>

| Status | Test                                  |
| :----: | ------------------------------------- |
|    ✅   | Auto-creation on user registration    |
|    ✅   | Profile listing & retrieval           |
|    ✅   | Restrict unauthorized updates/deletes |

</details>

<details>
<summary><strong>Events</strong></summary>

| Status | Test                                 |
| :----: | ------------------------------------ |
|    ✅   | Event CRUD operations                |
|    ✅   | Permissions respected for creators   |
|    ✅   | Handles valid/invalid IDs gracefully |

</details>

<details>
<summary><strong>Interested</strong></summary>

| Status | Test                             |
| :----: | -------------------------------- |
|    ✅   | CRUD operations & access control |
|    ✅   | Prevents duplicate interests     |

</details>

<details>
<summary><strong>Going</strong></summary>

| Status | Test                             |
| :----: | -------------------------------- |
|    ✅   | CRUD operations & validation     |
|    ✅   | Prevents duplicate going records |

</details>

<details>
<summary><strong>Comments</strong></summary>

| Status | Test                             |
| :----: | -------------------------------- |
|    ✅   | Comment creation, update, delete |
|    ✅   | Proper permission enforcement    |

</details>

<details>
<summary><strong>Reviews</strong></summary>

| Status | Test                                     |
| :----: | ---------------------------------------- |
|    ✅   | Review creation & rating logic           |
|    ✅   | Prevents multiple reviews per user/event |

</details>

<details>
<summary><strong>Followers</strong></summary>

| Status | Test                       |
| :----: | -------------------------- |
|    ✅   | Follower logic verified    |
|    ✅   | Prevents duplicate follows |

</details>

<details>
<summary><strong>Contact</strong></summary>

| Status | Test                                                    |
| :----: | ------------------------------------------------------- |
|    ❌   | Contact creation test (logged-in) not implemented fully |
|    ✅   | Permissions now prevent contact creation by guests      |

</details>

---

## 🧪 Manual Testing

Manual API endpoint testing was conducted using **Postman** and **Django Admin**, validating filtering, ordering, and permission logic beyond unit tests.

### Highlights:

* ✅ Ordering & filtering for profiles based on followers, events, going/interested counts, etc.
* ✅ Advanced event search: by tags, category, dates, title, owner
* ✅ Filter relationships (e.g., following/followed, interested/going events)
* ✅ Searchable events using nested fields like `owner__username`

---

## 🐞 Known Issues

### ✅ Resolved Bugs

1. **Taggit Integration Conflict**
   Despite using `blank=True`, tags remained a required field. Adjusted event creation tests to include the required tag field to resolve test failures.

2. **Followers Test Failure**
   Test failures traced back to a missing trailing slash in the profile list URL. Updating the route in `urls.py` fixed the issue.

3. **Contact App Test Behavior**
   Automatic test for contact creation failed due to incorrect permission settings. Initially believed to be a test error, but was later corrected by enforcing `IsAuthenticated` in the view permissions. Now functions as expected.

![Contact Test Fail](images/fail_create_contact_test.png)

---

🔙 [Back to README](README.md)

---


