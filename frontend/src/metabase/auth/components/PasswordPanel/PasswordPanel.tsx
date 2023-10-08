import { useCallback } from "react";
import { t } from "ttag";
import { useDispatch, useSelector } from "metabase/lib/redux";
import { login } from "../../actions";
import {
  getExternalAuthProviders,
  getHasSessionCookies,
  getIsLdapEnabled,
} from "../../selectors";
import type { LoginData } from "../../types";
import { AuthButton } from "../AuthButton";
import { LoginForm } from "../LoginForm";
import { ActionList, ActionListItem } from "./PasswordPanel.styled";

interface PasswordPanelProps {
  redirectUrl?: string;
}

export const PasswordPanel = ({ redirectUrl }: PasswordPanelProps) => {
  const providers = useSelector(getExternalAuthProviders);
  const isLdapEnabled = useSelector(getIsLdapEnabled);
  const hasSessionCookies = useSelector(getHasSessionCookies);
  const dispatch = useDispatch();

  const handleSubmit = useCallback(
    async (data: LoginData) => {
      await dispatch(login({ data, redirectUrl })).unwrap();
    },
    [dispatch, redirectUrl],
  );

  return (
    <div>
      <LoginForm
        isLdapEnabled={isLdapEnabled}
        hasSessionCookies={hasSessionCookies}
        onSubmit={handleSubmit}
      />
      <ActionList>
        <ActionListItem>
          <AuthButton link="/auth/forgot_password">
            {t`I seem to have forgotten my password`}
          </AuthButton>
	  <br />
	  <a target="_blank" style="font-weight: bold" href="http://200.137.215.27:5027/register-page">
           Ainda não é cadastrado? Registre-se aqui!
 	  </a>
        </ActionListItem>
        {providers.map(provider => (
          <ActionListItem key={provider.name}>
            <provider.Button redirectUrl={redirectUrl} />
          </ActionListItem>
        ))}
      </ActionList>
    </div>
  );
};
