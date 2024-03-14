<template>
    <div class="left_menu_admin_container">
        <h2>Админ панель портала 3S</h2>
        <ul class="left_side__list">
            <li><router-link to="/admin/">
                    <div class="left_side__list__item home"></div>
                    <span>Главная</span>
                </router-link>
            </li>
            <li><router-link to="/admin/statistics/">
                    <div class="left_side__list__item statistics"></div>
                    <span>Статистика</span>
                </router-link>
            </li>
            <li><router-link to="/admin/users/">
                    <div class="left_side__list__item users"></div>
                    <span>Пользователи</span>
                </router-link>
            </li>
        </ul>




    </div>
</template>





<style lang="scss">
.left_menu_admin_container {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 2;
    height: 100vh;
    background-color: $admin-left-side-background;
    width: 270px;

    & h2 {
        min-height: 5vh;
        display: flex;
        align-items: center;
        justify-content: center;

    }

    & ul {
        margin: 50px 0;

        & li {


            border-bottom: 2px solid $second-color;
            cursor: pointer;

            & a {
                width: 100%;
                height: 100%;
                padding: 20px 0 20px 20px;

                display: flex;
                align-items: center;
            }


            &:hover {
                background-color: $second-color;

                a {
                    color: $second-color-font;
                }
            }




            & .left_side__list__item {

                width: 25px;
                height: 25px;



                &.home {
                    background: url(@/assets/image/admin/home.svg);
                }

                &.statistics {
                    background: url(@/assets/image/admin/statistics.svg);
                }

                &.users {
                    background: url(@/assets/image/admin/user.svg);
                }

            }

            & span {
                margin-left: 10px;
            }

        }
    }
}
</style>