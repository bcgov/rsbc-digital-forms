import React, { useState, useEffect, useMemo } from "react";
import { Formik, Form as FormikForm } from "formik";
import { useNavigate } from "react-router-dom";
import BootstrapTable from 'react-bootstrap-table-next';
import filterFactory, { textFilter } from 'react-bootstrap-table2-filter';
import paginationFactory from 'react-bootstrap-table2-paginator';
import ToolkitProvider, { CSVExport } from 'react-bootstrap-table2-toolkit/dist/react-bootstrap-table2-toolkit';
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Modal from "react-bootstrap/Modal";
import Form from "react-bootstrap/Form";
import moment from "moment-timezone";
import Alert from "react-bootstrap/Alert";
import { useRecoilValue } from "recoil";
import { userRolesAtom } from "../../atoms/userRoles";
import { dateSortReactTable } from "../../utils/dateTime";
import { UserApi } from "../../api/userApi";
import { SearchableSelect } from "../common/Select/SearchableSelect";
import "./userAdminDashboard.scss";


export const UserAdminDashboard = () => {
  const initialValues = {
    user: {},
  };

  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);
  const [selectUsers, setSelectUsers] = useState([]);
  const [showConfirmModal, setShowConfirmModal] = useState(false);
  const [confirmAction, setConfirmAction] = useState(null);
  const [selectedUser, setSelectedUser] = useState(null);
  const [showNewUsersOnly, setShowNewUsersOnly] = useState(false);
  const [showAddAdminModal, setShowAddAdminModal] = useState(false);
  const userRoleData = useRecoilValue(userRolesAtom);
  const [successMessage, setSuccessMessage] = useState("");
  const [showSuccessMessage, setShowSuccessMessage] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (!userRoleData.some((role) => role["role_name"] === "administrator")) {
      navigate("/");
    } else {
      getAllUsers();
    }
  }, [userRoleData, navigate]);

  const addUniqueIds = (users) => {
    return users.map((user, index) => ({
      ...user,
      uniqueId: `${user.user_guid}-${index}`
    }));
  };

  const getAllUsers = () => {
    UserApi.getAll().then((resp) => {
      const uniqueUsers = addUniqueIds(resp.data);
      
      // Group users by user_guid
      const userGroups = uniqueUsers.reduce((groups, user) => {
        if (!groups[user.user_guid]) {
          groups[user.user_guid] = [];
        }
        groups[user.user_guid].push(user);
        return groups;
      }, {});
      
      // Filter out users who have at least one administrator role
      const filteredUsers = Object.values(userGroups)
        .filter(group => !group.some(user => user.role_name === "administrator"))
        .flatMap(group => group);
      
      setSelectUsers(
        filteredUsers
          .filter((user) => user.role_name === "officer")
          .map((user) => {
            return { label: user.login, value: user };
          })
      );
      
      setData(uniqueUsers);
      setLoading(false);
    });
  };

  const handleAddAdminConfirm = (values, { setSubmitting }) => {
    UserApi.postAdmin(values.user.value).then(() => {
      setSubmitting(false);
      getAllUsers();
      setShowAddAdminModal(false);
      showSuccess(`${values.user.value.first_name} ${values.user.value.last_name} has been successfully added as an administrator.`);
    });
  };

  const confirmDeleteUser = (user) => {
    setSelectedUser(user);
    setConfirmAction('delete');
    setShowConfirmModal(true);
  };

  const confirmApproveUser = (user) => {
    setSelectedUser(user);
    setConfirmAction('approve');
    setShowConfirmModal(true);
  };

  const handleConfirm = () => {
    if (confirmAction === 'delete') {
      deleteUser(selectedUser);
    } else if (confirmAction === 'approve') {
      approveUser(selectedUser);
    }
    setShowConfirmModal(false);
  };

  const deleteUser = (user) => {
    UserApi.delete(user).then(() => {
      setLoading(true);
      getAllUsers();
      showSuccess(`${user.first_name} ${user.last_name} has been successfully deleted.`);
    });
  };

  const approveUser = (user) => {
    UserApi.patch(user).then(() => {
      setLoading(true);
      getAllUsers();
      showSuccess(`${user.first_name} ${user.last_name} has been successfully approved.`);
    });
  };

  const showSuccess = (message) => {
    setSuccessMessage(message);
    setShowSuccessMessage(true);
    setTimeout(() => setShowSuccessMessage(false), 10000); // Hide after 10 seconds
  };

  const filteredData = useMemo(() => {
    if (showNewUsersOnly) {
      return data.filter(user => !user.approved_dt);
    }
    return data;
  }, [data, showNewUsersOnly]);

  const disableFilter = () => {
    setShowNewUsersOnly(false);
  };

  const paginationOptions = {
    sizePerPageList: [
      { text: '10', value: 10 },
      { text: '25', value: 25 },
      { text: '30', value: 30 },
      { text: '50', value: 50 }
    ],
    sizePerPage: 25,
    pageStartIndex: 1,
    paginationSize: 3,
    showTotal: true,
    withFirstAndLast: true,
    alwaysShowAllBtns: true,
    firstPageText: '<<',
    prePageText: '<',
    nextPageText: '>',
    lastPageText: '>>',
    nextPageTitle: 'First page',
    prePageTitle: 'Pre page',
    firstPageTitle: 'Next page',
    lastPageTitle: 'Last page',
    disablePageTitle: true,
    sizePerPageDropdownStyle: {
      display: 'inline-block',
      marginLeft: '5px',
      marginRight: '5px'
    }
  };

  const columns = [
    {
      dataField: 'last_name',
      text: 'SURNAME',
      sort: true,
      filter: textFilter(),
    },
    {
      dataField: 'first_name',
      text: 'Given',
      sort: true,
      filter: textFilter()
    },
    {
      dataField: 'badge_number',
      text: 'Prime ID',
      sort: true,
      filter: textFilter()
    },
    {
      dataField: 'agency',
      text: 'Agency',
      sort: true,
      filter: textFilter()
    },
    {
      dataField: 'user_guid',
      text: 'Keycloak GUID'
    },
    {
      dataField: 'login',
      text: 'Username'
    },
    {
      dataField: 'role_name',
      text: 'Role',
      sort: true,
      filter: textFilter()
    },
    {
      dataField: 'submitted_dt',
      text: 'Date Applied',
      sort: true,
      sortFunc: dateSortReactTable,
      formatter: (cell) => moment(cell).tz("America/Vancouver").format("YYYY-MM-DD HH:mm"),
      csvFormatter: (cell) => {
        if (cell === null || cell === undefined) {
          return '';
        }
        return moment(cell).tz("America/Vancouver").format("YYYY-MM-DD HH:mm");
      },
    },
    {
      dataField: 'last_active',
      text: 'Last Active',
      sort: true,
      sortFunc: dateSortReactTable,
      formatter: (cell) => {
        if (cell === null || cell === undefined) {
          return '';
        }
        return moment(cell).tz("America/Vancouver").format("YYYY-MM-DD HH:mm");
      },
      csvFormatter: (cell) => {
        if (cell === null || cell === undefined) {
          return '';
        }
        return moment(cell).tz("America/Vancouver").format("YYYY-MM-DD HH:mm");
      },
    },
    {
      dataField: 'action',
      text: 'Action',
      csvExport: false,  // This line excludes the column from CSV export
      formatter: (cellContent, row) => (
        row.approved_dt ? (
          <Button
            variant="danger"
            onClick={() => confirmDeleteUser(row)}
          >
            Delete
          </Button>
        ) : (
          <Button
            variant="success"
            onClick={() => confirmApproveUser(row)}
          >
            Approve
          </Button>
        )
      )
    }
  ];

  const ExportCSVButton = (props) => {
    const handleClick = () => {
      props.onExport();
    };
    return (
      <Button
        type="submit"
        variant="primary"
        size="sm"
        onClick={handleClick}
      >
        Export to CSV
      </Button>
    );
  };

  const renderTable = () => {
    if (filteredData.length === 0) {
      return (
        <div className="text-center p-3 bg-light border rounded">
          {showNewUsersOnly ? (
            <>
              <p>No pending user requests found. Please click 'Show All Users' to view all users.</p>
              <Button
                type="submit"
                variant="primary"
                size="sm"
                onClick={disableFilter}
              >
                Show All Users
              </Button>
            </>

          ) : (
            <p>No users found matching your search criteria. Please try adjusting your search parameters.</p>
          )}
        </div>
      );
    }
    const currentDateTime = moment().format('YYYY-MM-DD_HH-mm-ss');

    return (
      <ToolkitProvider
        keyField="uniqueId"
        data={filteredData}
        columns={columns}
        exportCSV={{
          fileName: `DF_User_List_${currentDateTime}.csv`,
          noAutoBOM: false,
          exportAll: false,
          onlyExportFiltered: true,
        }}
      >
        {
          props => (
            <div>
              <div className="d-flex justify-content-between align-items-center mb-3">
                <Form.Check
                  type="checkbox"
                  id="show-new-users-only"
                  label="Show New User Requests only"
                  checked={showNewUsersOnly}
                  onChange={(e) => setShowNewUsersOnly(e.target.checked)}
                />
                <ExportCSVButton { ...props.csvProps } />
              </div>
              <BootstrapTable
                { ...props.baseProps }
                filter={filterFactory()}
                sort={{ dataField: 'last_name', order: 'asc' }}
                striped
                wrapperClasses="table-responsive react-bootstrap-table"
                pagination={paginationFactory(paginationOptions)}
              />
            </div>
          )
        }
      </ToolkitProvider>
    );
  };

  if (isLoading) {
    return <div className="App">Loading...</div>;
  } else {
    return (
      <>
        {showSuccessMessage && (
          <Alert variant="success" onClose={() => setShowSuccessMessage(false)} dismissible>
            {successMessage}
          </Alert>
        )}
        <div className="border-design text-font">
          {renderTable()}
          <Formik initialValues={initialValues} onSubmit={(values, formikBag) => {
            setSelectedUser(values.user.value);
            setShowAddAdminModal(true);
          }}>
            {({ isSubmitting, values }) => (
              <FormikForm>
                <Container fluid>
                  <Row>
                    <Col sm={10}>
                      <SearchableSelect
                        label="Grant administrator role to selected user"
                        className="field-width field-height"
                        name="user"
                        options={selectUsers}
                      />
                    </Col>
                    <Col sm={2} className="top-margin">
                      <Button
                        type="submit"
                        variant="primary"
                        size="sm"
                        disabled={isSubmitting || !values.user.value}
                      >
                        Add as administrator
                      </Button>
                    </Col>
                  </Row>
                </Container>
              </FormikForm>
            )}
          </Formik>
        </div>

        <Modal show={showConfirmModal} onHide={() => setShowConfirmModal(false)}>
          <Modal.Header closeButton>
            <Modal.Title>Confirm Action</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            {confirmAction === 'delete'
              ? `Are you sure you want to delete the user ${selectedUser?.first_name} ${selectedUser?.last_name}?`
              : `Are you sure you want to approve the user ${selectedUser?.first_name} ${selectedUser?.last_name}?`
            }
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={() => setShowConfirmModal(false)}>
              Cancel
            </Button>
            <Button variant={confirmAction === 'delete' ? "danger" : "success"} onClick={handleConfirm}>
              Confirm
            </Button>
          </Modal.Footer>
        </Modal>
         
        <Modal show={showAddAdminModal} onHide={() => setShowAddAdminModal(false)}>
          <Modal.Header closeButton>
            <Modal.Title>Confirm Action</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            Are you sure you want to grant administrator role to {selectedUser?.first_name} {selectedUser?.last_name}?
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={() => setShowAddAdminModal(false)}>
              Cancel
            </Button>
            <Button variant="primary" onClick={() => {
              handleAddAdminConfirm({ user: { value: selectedUser } }, { setSubmitting: () => {} });
            }}>
              Confirm
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    );
  }
};