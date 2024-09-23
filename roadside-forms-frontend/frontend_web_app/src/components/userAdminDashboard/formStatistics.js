import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card, Alert } from 'react-bootstrap';
import { FormStatisticsApi } from '../../api/formStatisticsApi';
import './formStatistics.scss';

export const FormStatistics = () => {
  const [formData, setFormData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchFormStatistics();
  }, []);

  const fetchFormStatistics = async () => {
    try {
      const response = await FormStatisticsApi.getStatistics();
      if (response.status === 200) {
        setFormData(response.data);
      } else {
        throw new Error('Failed to fetch form statistics');
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const getStatusClass = (availableForms) => {
    if (availableForms < 50000) return 'danger';
    if (availableForms <= 60000) return 'warning';
    return 'success';
  };

  if (isLoading) {
    return <div className="text-center mt-5">Loading...</div>;
  }

  if (error) {
    return <Alert variant="danger">{error}</Alert>;
  }

  return (
    <Container fluid className="mt-4">
      <h1 className="mb-4">Form Inventory Dashboard</h1>
      <Row>
        {formData.map((form) => (
          <Col key={form.form_type} lg={6} className="mb-4">
            <Card>
              <Card.Header as="h5">{form.form_type} Forms</Card.Header>
              <Card.Body>
                <div className={`circle-container ${getStatusClass(form.available_forms)}`}>
                  <div className="circle total">
                    <span className="number">{form.total_forms}</span>
                    <span className="label">Total</span>
                  </div>
                  <div className="circle leased">
                    <span className="number">{form.leased_forms}</span>
                    <span className="label">Leased</span>
                  </div>
                  <div className="circle used">
                    <span className="number">{form.total_used_forms}</span>
                    <span className="label">Used</span>
                  </div>
                  <div className="circle available">
                    <span className="number">{form.available_forms}</span>
                    <span className="label">Available</span>
                  </div>
                </div>
                {form.available_forms < 50000 && (
                  <Alert variant="danger" className="mt-3">
                    Critical: Available forms are below 50,000!
                  </Alert>
                )}
                {form.available_forms >= 50000 && form.available_forms <= 60000 && (
                  <Alert variant="warning" className="mt-3">
                    Warning: Available forms are between 50,000 and 60,000!
                  </Alert>
                )}
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
};