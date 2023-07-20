import React, {useState,useEffect} from 'react';
import { Formik, Form} from 'formik';
import { useNavigate} from 'react-router-dom';
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import moment from 'moment-timezone';
import { useRecoilValue } from 'recoil';
import { userRolesAtom } from '../../atoms/userRoles';


import { UserApi } from '../../api/userApi';
import { SearchableSelect } from '../common/Select/SearchableSelect';
import './userAdminDashboard.scss';

export const UserAdminDashboard = () => {

    const initialValues = {
      user:{},
    };

    const [isLoading, setLoading] = useState(true)
    const [data, setData] = useState({});
    const [selectUsers, setSelectUsers] = useState([]);
    const userRoleData = useRecoilValue(userRolesAtom)
    const navigate = useNavigate();
    
    useEffect(() => {
      if(!userRoleData.some( role => role['role_name'] === 'administrator' )){
        navigate("/")
      }else{
      getAllUsers();
      }
    }, [userRoleData,navigate]);
    
    const getAllUsers = () =>{
      UserApi.getAll().then( (resp) => {
        setSelectUsers(resp.data.filter(user => user.role_name === "officer" ).map((user) => { return ({"label":user.login,"value":user})}));
        setData(resp.data);
        setLoading(false);
      })
    }

    const deleteUser = (user) => {
      UserApi.delete(user).then(()=>{
        setLoading(true);
        getAllUsers();
      })
    }
    
    const approveUser = (user) => {
      UserApi.patch(user).then(()=>{
        setLoading(true);
        getAllUsers();
      })
    }

    const onSubmit = (values, { setSubmitting }) => {
      UserApi.postAdmin(values.user).then(() => {
        setSubmitting(false);
        getAllUsers();
      })
      
    }
  
    if(isLoading){
      return <div className="App">Loading...</div>;
    }else{
      return (
        <>
          <div className='border-design text-font'>
          <Table>
            <thead>
              <tr>
                <th>SURNAME</th>
                <th>Given</th>
                <th>Prime ID</th>
                <th>Agency</th>
                <th>Keycloak GUID</th>
                <th>Username</th>
                <th>Role</th>
                <th>Date Applied</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {data && data.map((user) => (
                <tr key={`${user.user_guid}-${user.role_name}`}>
                  <td>{user.last_name}</td>
                  <td>{user.first_name}</td>
                  <td>{user.badge_number}</td>
                  <td>{user.agency}</td>
                  <td>{user.user_guid}</td>
                  <td>{user.login}</td>
                  <td>{user.role_name}</td>
                  <td className="text-muted small">{moment(user.submitted_dt).tz("America/Vancouver").format("YYYY-MM-DD HH:mm")}</td>
                  <td>{user.approved_dt ? <Button variant="danger" onClick={() => {deleteUser(user)}} >Delete</Button> : <Button variant="success" onClick={() => {approveUser(user)}} >Approve</Button>}</td>
                </tr>
              ))}
            </tbody>
          </Table>
          <Formik initialValues={initialValues} onSubmit={onSubmit}>
          {({ isSubmitting }) => (
            <Form>
              <Container fluid>
                <Row>
                  <Col sm={10}>
                    <SearchableSelect label="Grant administrator role to selected user" className="field-width field-height" name="user" options={selectUsers} />
                  </Col>
                  <Col sm={2} className="top-margin">
                    <Button type="submit" variant="primary" size="sm" disabled={isSubmitting}>Add as administrator</Button>
                  </Col>
                </Row>
              </Container>
            </Form>
          )}
          </Formik>
        </div>
      </>
      );
    }
  }
