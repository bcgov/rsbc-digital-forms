import React from "react";
import { render, act } from "@testing-library/react";
import { RecoilRoot } from "recoil";
import { userRolesAtom } from "../../../atoms/userRoles";
import { loginCompletedAtom } from "../../../atoms/loginCompleted";
import { useNavigate } from "react-router-dom";
import { UserApi } from "../../../api/userApi";
import { UserAdminDashboard } from "../../../components/userAdminDashboard/userAdminDashboard";

jest.mock("react-router-dom", () => ({
  ...jest.requireActual("react-router-dom"),
  useNavigate: jest.fn(),
}));

describe("UserAdminDashboard component", () => {
  test("should match snapshot", async () => {
    const mockNavigate = jest.fn();

    UserApi.getAll = jest.fn().mockResolvedValue({
      data: [
        {
          agency: "BCHP Burnaby",
          approved_dt: "Thu, 22 Jun 2023 16:51:39 GMT",
          badge_number: "222222",
          display_name: "Test, user",
          first_name: "USER",
          last_name: "Test",
          login: "TEST@idir",
          role_name: "administrator",
          submitted_dt: "Thu, 22 Jun 2023 16:51:39 GMT",
          user_guid: "91D388D1339C41388E622F5",
          username: "91d388d1339c41388e622f5@idir",
        },
        {
          agency: "BCHP Burnaby",
          approved_dt: "Thu, 22 Jun 2023 16:51:39 GMT",
          badge_number: "222222",
          display_name: "Test, user",
          first_name: "USER",
          last_name: "Test",
          login: "TEST@idir",
          role_name: "officer",
          submitted_dt: "Thu, 22 Jun 2023 16:51:39 GMT",
          user_guid: "91D388D1339C41388E622F5",
          username: "91d388d1339c41388e622f5@idir",
        },
      ],
    });

    const setSelectUsersMock = jest.fn();
    const setDataMock = jest.fn();
    const setLoadingMock = jest.fn();

    useNavigate.mockImplementation(() => mockNavigate);

    let container;

    await act(async () => {
      ({ container } = render(
        <RecoilRoot
          initializeState={(snap) => {
            snap.set(userRolesAtom, [
              {
                approved_dt: "Mon, 05 Jun 2023 14:27:31 GMT",
                role_name: "administrator",
                submitted_dt: "Thu, 01 Jun 2023 09:39:42 GMT",
                user_guid: "91d388d1889c87654e622f5e9@idir",
              },
            ]);
            snap.set(loginCompletedAtom, true);
          }}
        >
          <UserAdminDashboard
            setLoading={setLoadingMock}
            setSelectUsers={setSelectUsersMock}
            setData={setDataMock}
          />
        </RecoilRoot>,
      ));
    });

    expect(container).toMatchSnapshot();
  });
});
