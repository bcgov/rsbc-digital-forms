import { render, fireEvent, act } from "@testing-library/react";
import { RecoilRoot } from "recoil";
import { RequestAccess } from "../../../components/RequestAccess/requestAccess";

import { StaticDataApi } from "../../../api/staticDataApi";
import { userRolesAtom } from "../../../atoms/userRoles";
import { loginCompletedAtom } from "../../../atoms/loginCompleted";

// Mocking useNavigate
jest.mock("react-router-dom", () => ({
  ...jest.requireActual("react-router-dom"),
  useNavigate: jest.fn(),
}));

describe("RequestAccess component", () => {
  test("should match snapshot", async () => {
    const handleClickMock = jest.fn();
    StaticDataApi.get = jest.fn().mockResolvedValue({
      data: [
        {
          vjur: "AB",
          agency_name: "Test ag.",
        },
        {
          vjur: "ABC",
          agency_name: "Test ag 1.",
        },
      ],
    });
    const setAgencyMock = jest.fn();
    const setOptionsMock = jest.fn();

    const { container, findByText } = render(
      <RecoilRoot
        initializeState={(snap) => {
          snap.set(userRolesAtom, []);
          snap.set(loginCompletedAtom, true);
        }}
      >
        <RequestAccess
          handleClick={handleClickMock}
          setAgency={setAgencyMock}
          setOptions={setOptionsMock}
        />
      </RecoilRoot>,
    );

    const button = await findByText("Apply for Access");
    await act(async () => {
      fireEvent.click(button);
      await Promise.resolve();
    });

    expect(container).toMatchSnapshot();
  });
});
